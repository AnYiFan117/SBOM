import subprocess, json, os

# 定义要执行的命令
cmd = ["python3", "-m", "cyclonedx_py", "environment"]

def generate_sbom(project_path: str):
    """
    针对 Python 项目生成 SBOM。
    实际场景下可以通过 subprocess 调用 cyclonedx-py 命令
    """
    print(f"正在为 Python 项目 {project_path} 生成 SBOM...")
    try: 
        # 安装CycloneDX SBOM生成工具
        print("正在安装CycloneDX SBOM生成工具...")
        os.system("pip install cyclonedx-bom")
        # 进入项目目录
        os.chdir(project_path)
        # 生成SBOM
        print("正在生成SBOM...")
        # 使用 subprocess.run 来执行命令，并捕获输出（注意设置 text=True 得到字符串输出）
        result = subprocess.run(cmd, capture_output=True, text=True)

        # 判断命令是否执行成功
        if result.returncode != 0:
            print("命令执行错误：", result.stderr)
        else:
            output = result.stdout
            try:
                # 尝试将输出解析为 JSON 数据
                data = json.loads(output)
            except json.JSONDecodeError:
                # 如果解析失败，可将原始输出作为字符串保存到 JSON 文件中
                data = {"output": output}

            # 将数据写入 JSON 文件
            with open("SBOM.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print("SBOM 已保存到 SBOM.json 文件中")
    except Exception as e:
        print(f"生成 SBOM 失败：{e}")
    
        
