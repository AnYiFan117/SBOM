import os, subprocess, json

def generate_sbom(project_path: str, command: str):
    """
    针对 Go 项目生成 SBOM。
    可通过调用 cyclonedx-maven-plugin 或其他工具实现
    """
    print(f"正在为 Go 项目 {project_path} 生成 SBOM...")
    try:
        # 先安装go
        # print("正在安装go...")
        # os.system("sudo apt-get install -y golang")
        # 进入目录
        print("请自行安装Golang version>=1.18")
        os.chdir(project_path)
        # 安装SBOM工具
        # print("正在安装SBOM工具...")
        # os.system("go install github.com/ozonru/cyclonedx-go/cmd/cyclonedx-go@latest")
        # 执行
        print("正在执行...")
        result = subprocess.run(command, shell=True, check=True)
        print(f"SBOM生成完毕，保存在sbom.json中")
    except Exception as e:
        print("请检查在环境中是否有Golang")
        print(f"SBOM生成失败：{e}")
        
