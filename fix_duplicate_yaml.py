#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复addlaws文件夹内重复YAML元数据的脚本
"""

import os

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
                lines = f.readlines()
            
            if not lines:
                continue
            
            # 检查是否有重复的YAML元数据
            yaml_count = 0
            yaml_end_pos = -1
            
            for i, line in enumerate(lines):
                stripped_line = line.strip()
                if stripped_line == "---":
                    yaml_count += 1
                    if yaml_count == 2:
                        yaml_end_pos = i
                    elif yaml_count > 2:
                        # 找到重复的YAML元数据，需要修复
                        print(f"  Found duplicate YAML sections in {file_path}")
                        
                        # 重新构建文件内容：只保留第一个YAML元数据和后续内容
                        new_lines = lines[:yaml_end_pos+1]  # 保留第一个YAML元数据
                        
                        # 跳过中间的内容，直到找到第二个---之后的内容
                        # 从yaml_end_pos+1开始查找，直到找到下一个---，然后跳过到下一行
                        skip_mode = True
                        for j in range(yaml_end_pos+1, len(lines)):
                            if skip_mode:
                                if lines[j].strip() == "---":
                                    # 找到第二个---，跳过它
                                    skip_mode = False
                            else:
                                new_lines.append(lines[j])
                        
                        # 写入修复后的内容
                        with open(file_path, "w", encoding=ENCODING) as f:
                            f.writelines(new_lines)
                        
                        print(f"  Fixed duplicate YAML sections in {file_path}")
                        break

print("All files processed!")
