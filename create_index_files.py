import os

def create_index_files(parent_dir):
    """递归地为指定目录下的所有子目录创建_index.md文件"""
    # 检查父目录是否存在
    if not os.path.exists(parent_dir):
        print(f"目录不存在: {parent_dir}")
        return 0, 0
    
    created_count = 0
    exists_count = 0
    
    # 遍历目录下的所有项目
    for item in os.listdir(parent_dir):
        item_path = os.path.join(parent_dir, item)
        
        # 如果是目录
        if os.path.isdir(item_path):
            # 为当前目录创建_index.md文件
            index_file_path = os.path.join(item_path, "_index.md")
            
            # 检查_index.md文件是否已存在
            if os.path.exists(index_file_path):
                print(f"已存在: {index_file_path}")
                exists_count += 1
            else:
                # 创建_index.md文件内容
                content = f"""---
title: {item}
linkTitle: {item}
type: "docs"
cascade: {{ type: "docs" }}
---
"""
                
                # 写入文件
                try:
                    with open(index_file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"已创建: {index_file_path}")
                    created_count += 1
                except Exception as e:
                    print(f"创建失败 {index_file_path}: {str(e)}")
            
            # 递归处理子目录
            sub_created, sub_exists = create_index_files(item_path)
            created_count += sub_created
            exists_count += sub_exists
    
    return created_count, exists_count

if __name__ == "__main__":
    total_created = 0
    total_exists = 0
    
    # 为行政执法目录创建文件
    print("=== 处理行政执法目录 ===")
    created, exists = create_index_files("content/行政执法")
    total_created += created
    total_exists += exists
    print(f"行政执法目录: 创建了 {created} 个文件，跳过了 {exists} 个已存在的文件")
    
    # 为行政执法合规目录创建文件
    print("\n=== 处理行政执法合规目录 ===")
    created, exists = create_index_files("content/行政执法合规")
    total_created += created
    total_exists += exists
    print(f"行政执法合规目录: 创建了 {created} 个文件，跳过了 {exists} 个已存在的文件")
    
    print(f"\n=== 总计 ===")
    print(f"总共创建了 {total_created} 个文件，跳过了 {total_exists} 个已存在的文件")
