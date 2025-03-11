import os
import sys

# 获取当前 main.py 所在目录（src 文件夹）
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取上级目录（项目根目录）
parent_dir = os.path.dirname(current_dir)
# 将项目根目录添加到 sys.path 中
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

config_path = os.path.join(parent_dir, "config.yaml")

import argparse
from myutils.load_config import load_myconfig
from sbom_tools import python_tool, go_tool, java_tool

def main():
    parser = argparse.ArgumentParser(description="统一SBOM管理程序")
    parser.add_argument("project_path", help="待分析的项目目录路径")
    parser.add_argument("--language", help="指定项目使用的语言")
    args = parser.parse_args()

    

    project_path = args.project_path
    project_language = args.language

    if not os.path.isdir(project_path):
        print(f"错误：{project_path} 不是一个有效的目录")
        sys.exit(1)

    # 检测项目使用的语言
    language = project_language
    print("检测到的项目语言：", language)

    config = load_myconfig(config_path)
    print(config['tools']['python'])

    # 根据检测结果调用对应的 SBOM 生成工具
    if language == 'python':
        python_tool.generate_sbom(project_path, config['tools']['python'])
    elif language == 'go':
        go_tool.generate_sbom(project_path, config['tools']['go'])
    elif language == 'java':
        java_tool.generate_sbom(project_path, config['tools']['java'])
    else:
        print("未识别项目的有效语言，或暂不支持该语言")
        sys.exit(1)

if __name__ == "__main__":
    main()
