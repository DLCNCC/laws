#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清理文件中的重复目录
"""

import os
import re

# 配置
ADDLAWS_DIR = "./addlaws"
ENCODING = "utf-8"

# 遍历文件
for root, dirs, files in os.walk(ADDLAWS_DIR):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            print(f"Processing: {file_path}")
            
            # 读取文件内容
            with open(file_path, "r", encoding=ENCODING) as f:
                content = f.read()
            
            lines = content.splitlines()
            new_lines = []
            toc_count = 0
            in_toc = False
            
            for line in lines:
                # 检查是否是目录标题
                if line == "## 目录":
                    toc_count += 1
                    # 如果已经有一个目录，跳过这个目录
                    if toc_count > 1:
                        in_toc = True
                        continue
                
                # 如果在跳过的目录中，检查是否到了目录结束（遇到---）
                if in_toc:
                    if line == "---":
                        # 跳过当前的---和后面的空行
                        in_toc = False
                    continue
                
                new_lines.append(line)
            
            # 保存文件
            with open(file_path, "w", encoding=ENCODING) as f:
                f.write("\n".join(new_lines))
            
            print(f"Processed: {file_path}")

print("All files processed!")
