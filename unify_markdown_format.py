#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一addlaws文件夹内Markdown文件格式脚本

功能：
1. 遍历addlaws文件夹内所有Markdown文件
2. 备份原始文件
3. 添加YAML前置元数据
4. 统一标题层级
5. 生成目录
6. 规范文本排版
7. 统一条款格式
8. 规范列表样式
"""

import os
import re
import uuid
import shutil
from datetime import datetime
import urllib.parse
import yaml
import requests
from bs4 import BeautifulSoup

# 配置
ADDLAWS_DIR = "./addlaws"
BACKUP_DIR = "./addlaws_backup"
ENCODING = "utf-8"
URL_MAPPING_FILE = "./url_mapping.yaml"

# URL模板配置
# 根据法律法规类型使用不同的数据库
URL_TEMPLATES = {
    "default": "https://flk.npc.gov.cn/",  # 国家法律法规数据库
    "law": "https://flk.npc.gov.cn/",  # 法律
    "regulation": "http://xzfg.moj.gov.cn/search2.html?keyword={title}",  # 行政法规
    "rule": "https://www.gov.cn/zhengce/xxgk/gjgzk/index.htm?searchWord={title}"  # 部门规章
}

# 创建备份目录
os.makedirs(BACKUP_DIR, exist_ok=True)

# 正则表达式
RE_LEGAL_NAME = r"^#\s+(.*)"
RE_CHAPTER = r"^第[一二三四五六七八九十百千]+章\s+.*"
RE_SECTION = r"^第[一二三四五六七八九十百千]+节\s+.*"
RE_ARTICLE = r"^第[一二三四五六七八九十百千\d]+条\s+"
RE_LIST_ITEM = r"^\s*(\(\d+\)|\(一\)|\(二\)|\(三\)|\(四\)|\(五\)|\(六\)|\(七\)|\(八\)|\(九\)|\(十\)|\(十一\)|\(十二\)|\(十三\)|\(十四\)|\(十五\)|\(十六\)|\(十七\)|\(十八\)|\(十九\)|\(二十\))\s*"
RE_PASSAGE_INFO = r"^\((.*)\)"
RE_DATE = r"(19|20)\d{2}年\d{1,2}月\d{1,2}日"

# 读取URL映射表
def read_url_mapping():
    if os.path.exists(URL_MAPPING_FILE):
        with open(URL_MAPPING_FILE, 'r', encoding=ENCODING) as f:
            return yaml.safe_load(f) or {}
    return {}

# 搜索国家法律法规数据库，获取最终URL
def search_law_url(title):
    """
    搜索国家法律法规数据库，获取法律文件的最终URL
    
    Args:
        title: 法律文件标题
        
    Returns:
        str: 法律文件的最终URL，如果搜索失败则返回国家法律法规数据库主页URL
    """
    try:
        # 尝试使用更真实的浏览器请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1"
        }
        
        # 使用session来保持cookies
        session = requests.Session()
        
        # 首先访问主页，获取初始cookies
        session.get("https://flk.npc.gov.cn/", headers=headers, timeout=10)
        
        # 然后进行搜索
        search_url = "https://flk.npc.gov.cn/search"
        params = {
            "searchWord": title
        }
        response = session.get(search_url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        
        # 解析搜索结果
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 查找搜索结果列表
        # 尝试多种方式查找结果
        # 1. 查找所有链接
        links = soup.find_all("a")
        
        # 2. 查找带有特定class或id的元素
        result_containers = soup.find_all(class_=re.compile(r"result|search|item"))
        for container in result_containers:
            container_links = container.find_all("a")
            links.extend(container_links)
        
        # 去重
        unique_links = list({link["href"]: link for link in links if "href" in link.attrs}.values())
        
        # 遍历所有链接，寻找最相关的结果
        for link in unique_links:
            href = link["href"]
            text = link.get_text().strip()
            
            # 检查链接是否可能是detail页面
            if "detail" in href:
                # 如果是相对URL，转换为绝对URL
                if href.startswith("/"):
                    return f"https://flk.npc.gov.cn{href}"
                elif "flk.npc.gov.cn" in href:
                    return href
            
            # 检查链接文本是否包含标题的关键词
            elif any(keyword in text for keyword in title.split()) and len(text) > 10:
                # 如果是相对URL，转换为绝对URL
                if href.startswith("/"):
                    return f"https://flk.npc.gov.cn{href}"
                elif "flk.npc.gov.cn" in href:
                    return href
        
        # 如果没有找到结果，尝试使用直接的detail页面格式
        # 国家法律法规数据库的detail页面格式可能是固定的
        # 尝试使用不同的detail页面格式，优先使用detail.html
        detail_formats = [
            "https://flk.npc.gov.cn/detail.html?searchWord={title}",
            "https://flk.npc.gov.cn/detail2.html?searchWord={title}",
            "https://flk.npc.gov.cn/search?searchWord={title}"
        ]
        
        for fmt in detail_formats:
            encoded_title = urllib.parse.quote(title)
            test_url = fmt.format(title=encoded_title)
            # 对于detail.html，我们直接返回，因为它是最可能的最终地址
            if "detail.html" in fmt:
                return test_url
            try:
                test_response = session.head(test_url, headers=headers, timeout=5)
                if test_response.status_code == 200:
                    return test_url
            except:
                continue
        
        # 如果还是没有找到，返回detail.html页面，这是最可能的最终地址
        encoded_title = urllib.parse.quote(title)
        return f"https://flk.npc.gov.cn/detail.html?searchWord={encoded_title}"
    except Exception as e:
        print(f"搜索法律URL失败：{title} - {e}")
        # 发生错误时返回detail.html页面
        encoded_title = urllib.parse.quote(title)
        return f"https://flk.npc.gov.cn/detail.html?searchWord={encoded_title}"

# 根据文件信息生成URL
def generate_url(title, file_path):
    # 读取URL映射表
    url_mapping = read_url_mapping()
    
    # 检查映射表中是否存在对应的URL
    if title in url_mapping:
        return url_mapping[title]
    
    # 搜索国家法律法规数据库，获取最终URL
    final_url = search_law_url(title)
    
    # 返回最终URL
    return final_url

# 提取年份信息
def extract_years(content):
    years = set()
    # 从日期中提取年份
    matches = re.findall(RE_DATE, content)
    for match in matches:
        # match是一个元组，第一个元素是"19"或"20"，第二个元素是年份的后两位
        if isinstance(match, tuple):
            year = match[0] + match[1] if len(match) > 1 else match[0]
        else:
            year = match[:4]
        years.add(year)
    
    # 从文件名中提取年份
    # 简单的年份提取，可根据实际需要调整
    year_match = re.search(r"(19|20)\d{2}", content)
    if year_match:
        years.add(year_match.group(0))
    
    return list(years)

# 提取关键词
def extract_keywords(title, content):
    keywords = set()
    
    # 从标题中提取关键词
    title_keywords = re.findall(r"[\u4e00-\u9fa5]{2,}", title)
    keywords.update(title_keywords)
    
    # 从内容中提取关键词（简单实现，可根据实际需要调整）
    # 提取法律相关的高频词
    legal_keywords = ["法律", "法规", "条例", "办法", "规定", "实施", "管理", "处罚", "行政", "责任"]
    for keyword in legal_keywords:
        if keyword in content:
            keywords.add(keyword)
    
    return list(keywords)[:5]  # 最多提取5个关键词

# 遍历文件
for root, dirs, files in os.walk(ADDLAWS_DIR):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            backup_path = os.path.join(BACKUP_DIR, file_path.replace(ADDLAWS_DIR, "", 1).lstrip(os.sep))
            
            # 创建备份目录
            os.makedirs(os.path.dirname(backup_path), exist_ok=True)
            
            # 备份文件
            shutil.copy2(file_path, backup_path)
            
            print(f"Processing: {file_path}")
            
            # 读取文件内容
            with open(file_path, "r", encoding=ENCODING) as f:
                content = f.read()
            
            lines = content.splitlines()
            new_lines = []
            
            # 1. 检查是否已经有YAML元数据
            has_yaml = False
            yaml_end_index = -1
            if lines and lines[0] == '---':
                has_yaml = True
                # 找到YAML结束标记
                for i, line in enumerate(lines[1:], 1):
                    if line == '---':
                        yaml_end_index = i
                        break
            
            # 生成新的YAML元数据
            legal_name = file[:-3]  # 去除.md后缀
            
            # 从文件名提取信息
            file_id = str(uuid.uuid4())
            title = legal_name
            link_title = legal_name
            
            # 生成URL
            url = generate_url(title, file_path)
            
            # 提取年份信息
            years = extract_years(content)
            
            # 提取关键词
            keywords = extract_keywords(title, content)
            
            # 从文件路径提取group和categories
            # 解析文件路径，提取目录结构
            relative_path = os.path.relpath(file_path, ADDLAWS_DIR)
            path_parts = relative_path.split(os.sep)
            
            group = path_parts[0] if len(path_parts) > 0 else ""
            categories = path_parts[1] if len(path_parts) > 1 else ""
            
            # 调整tags
            tags = []
            if "条例" in title:
                tags.append("条例")
            if "办法" in title:
                tags.append("办法")
            if "规定" in title:
                tags.append("规定")
            if "细则" in title:
                tags.append("细则")
            
            # 调整years
            formatted_years = [f"{year}年" for year in years]
            
            # 生成LinkTitle
            link_title = title
            
            # 生成YAML元数据
            yaml_meta = f"""---
id: {file_id}
title: {title}
LinkTitle: {link_title}
file: {file}
author: 
date: '{datetime.now().strftime('%Y-%m-%d')}'
publication_date: ''
effective_date: ''
status: 有效
group: {group}
categories:
  - {categories}
tags:
  - {group}
  - 有效
  - {tags[0] if tags else ''}
years:
  - {formatted_years[0] if formatted_years else ''}
keywords:
  - {keywords[0] if keywords else ''}
  - {keywords[1] if len(keywords) > 1 else ''}
  - {keywords[2] if len(keywords) > 2 else ''}
  - {keywords[3] if len(keywords) > 3 else ''}
  - {keywords[4] if len(keywords) > 4 else ''}
urls:
  - {url}
---
"""
            
            # 如果有YAML元数据，替换它；否则，添加它
            content_lines = []
            if has_yaml and yaml_end_index != -1:
                # 跳过旧的YAML内容，只处理实际内容
                content_lines = lines[yaml_end_index+1:]
            else:
                # 处理所有内容
                content_lines = lines
            
            # 标记变量
            has_legal_name = False
            chapters = []
            sections = []
            in_legal_name = False
            in_passage_info = False
            
            # 处理文件内容
            processed_lines = []
            for line in content_lines:
                stripped_line = line.strip()
                
                # 跳过空行
                if not stripped_line:
                    processed_lines.append("")
                    continue
                
                # 处理法律名称
                if not has_legal_name:
                    match = re.match(RE_LEGAL_NAME, line)
                    if match:
                        legal_name = match.group(1)
                        processed_lines.append(f"**{legal_name}**")
                        has_legal_name = True
                        in_legal_name = True
                        continue
                
                # 处理法律通过信息
                if in_legal_name:
                    match = re.match(RE_PASSAGE_INFO, line)
                    if match:
                        processed_lines.append(f"> {line}")
                        in_passage_info = True
                        continue
                    elif in_passage_info and "根据" in line and "修正" in line:
                        processed_lines.append(f"> {line}")
                        continue
                    else:
                        in_legal_name = False
                        in_passage_info = False
                
                # 处理章节
                # 匹配原始章节标题（如"第一章 总 则"）或转换后的章节标题（如"## 第一章 总 则"）
                chapter_match = re.match(r"^(##\s*)?第[一二三四五六七八九十百千]+章\s*.*", line)
                if chapter_match:
                    # 提取章节标题，去除可能的"## "前缀
                    chapter_title = re.sub(r"^##\s*", "", line).strip()
                    chapters.append(chapter_title)
                    # 确保使用正确的格式
                    processed_lines.append(f"## {chapter_title}")
                    continue
                
                # 处理节
                # 匹配原始节标题（如"第一节 总则"）或转换后的节标题（如"### 第一节 总则"）
                section_match = re.match(r"^(###\s*)?第[一二三四五六七八九十百千]+节\s*.*", line)
                if section_match:
                    # 提取节标题，去除可能的"### "前缀
                    section_title = re.sub(r"^###\s*", "", line).strip()
                    sections.append(section_title)
                    # 确保使用正确的格式
                    processed_lines.append(f"### {section_title}")
                    continue
                
                # 处理条款
                article_match = re.match(RE_ARTICLE, stripped_line)
                if article_match:
                    article_full = article_match.group(0).strip()
                    article_content = stripped_line[article_match.end():]
                    processed_lines.append(f"- **{article_full}**  {article_content}")
                    continue
                
                # 处理阿拉伯数字开头的条款（如"1. 内容"或"1 内容"）
                article_match_num = re.match(r"^(\d+)\s*[.。]?\s+", stripped_line)
                if article_match_num:
                    article_num = article_match_num.group(1)
                    article_content = stripped_line[article_match_num.end():]
                    processed_lines.append(f"- **第{article_num}条**  {article_content}")
                    continue
                
                # 处理列表项
                list_match = re.match(RE_LIST_ITEM, stripped_line)
                if list_match:
                    processed_lines.append(f"- {stripped_line}")
                    continue
                
                # 处理其他格式的列表项（如"1. 内容"或"一、内容"）
                other_list_match = re.match(r"^\s*(\d+\s*[.。]|(?:[一二三四五六七八九十百千]+|\w+)\s*[、.。])\s+", stripped_line)
                if other_list_match:
                    processed_lines.append(f"- {stripped_line}")
                    continue
                
                # 默认情况
                processed_lines.append(line)
            
            # 合并YAML和处理后的内容
            new_lines = [yaml_meta] + processed_lines
            
            # 移除可能的目录
            # 遍历新生成的行，移除目录相关内容
            final_lines = []
            in_toc = False
            for line in new_lines:
                # 检查是否是目录标题
                if line == "## 目录":
                    in_toc = True
                    continue
                
                # 如果在目录中，检查是否到了目录结束（遇到---）
                if in_toc:
                    if line == "---":
                        # 跳过当前的---和后面的空行
                        in_toc = False
                    continue
                
                final_lines.append(line)
            
            # 替换为最终的行
            new_lines = final_lines
            
            # 4. 保存文件
            with open(file_path, "w", encoding=ENCODING) as f:
                f.write("\n".join(new_lines))
            
            print(f"Processed: {file_path}")

print("All files processed!")
print(f"Backup files are in: {BACKUP_DIR}")