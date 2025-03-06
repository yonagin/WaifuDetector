import os
import shutil
import argparse


def extract_files_recursively(source_dir, target_dir):
    """
    递归提取源目录中的所有文件并平铺到目标目录
    """

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 计数器用于处理重名文件
    file_count = 0

    # 遍历源目录
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)

            # 获取文件名和扩展名
            file_name, file_ext = os.path.splitext(file)
            target_file_path = os.path.join(target_dir, file)

            # 处理重名文件
            while os.path.exists(target_file_path):
                file_count += 1
                target_file_path = os.path.join(target_dir, f"{file_name}_{file_count}{file_ext}")

            # 复制文件
            shutil.copy2(source_file_path, target_file_path)
            print(f"已复制: {source_file_path} -> {target_file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="递归提取文件夹中的所有文件并平铺到指定目录")
    parser.add_argument("--source", type=str, help="源文件夹路径")
    parser.add_argument("--target",  type=str,  help="目标文件夹路径")

    args = parser.parse_args()

    extract_files_recursively(args.source, args.target)
    print("所有文件已成功提取！")