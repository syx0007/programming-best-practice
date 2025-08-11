#!/usr/bin/env python3
import os
from pathlib import Path

def generate_directory_tree(root_dir="src", output_file="SUMMARY.md"):
    """
    递归生成带路径的目录树结构并保存为Markdown文件
    
    参数:
        root_dir: 要扫描的根目录 (默认: 'src')
        output_file: 输出文件路径 (默认: 'SUMMARY.md')
    """
    root_path = Path(root_dir)
    
    if not root_path.exists():
        print(f"错误: 目录 '{root_dir}' 不存在")
        return
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 目录结构\n\n")
        
        # 存储所有文件和它们的相对路径
        file_entries = []
        
        # 递归收集所有文件
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith('.md'):  # 只处理Markdown文件
                    file_path = Path(dirpath) / filename
                    rel_path = os.path.relpath(file_path, root_dir)
                    file_entries.append((dirpath, filename, rel_path))
        
        # 按目录层级和文件名排序
        file_entries.sort(key=lambda x: (x[0], x[1].lower()))
        
        current_dir = None
        for dirpath, filename, rel_path in file_entries:
            # 如果目录改变了，添加目录标题
            if dirpath != current_dir:
                if current_dir is not None:
                    f.write("\n")
                # 显示相对于root_dir的目录路径
                rel_dir = os.path.relpath(dirpath, root_dir)
                if rel_dir == ".":
                    f.write("# 根目录\n")
                else:
                    f.write(f"# {rel_dir.replace(os.sep, '/')}\n")
                current_dir = dirpath
            
            # 写入文件项
            f.write(f"- [{filename}](./{rel_path.replace(os.sep, '/')})\n")
        
        print(f"目录树已生成到 {output_file}")

if __name__ == "__main__":
    generate_directory_tree()
