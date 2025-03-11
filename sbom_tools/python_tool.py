import subprocess, json, os

params = ["environment", "requirements", "pipenv", "poetry"]

def generate_sbom(project_path: str, command: str):
    """
    针对 Python 项目生成 SBOM。
    实际场景下可以通过 subprocess 调用 cyclonedx-py 命令
    """
    print(f"正在为 Python 项目 {project_path} 生成 SBOM...")
    print(f"python项目需要对待测项进行选择，请在如下参数中选择：")
    for param in params:
        print(f"{param}", end=", ")
    # 获取控制台输入
    while 1:
        param = input("请输入参数：")
        if param not in params:
            print("参数错误，请重新输入！")
        else:
            command+=f" {param}"
            break
    try: 
        # 安装CycloneDX SBOM生成工具
        # print("正在安装CycloneDX SBOM生成工具...")
        # os.system("pip install cyclonedx-bom")
        # 进入项目目录
        os.chdir(project_path)
        # 生成SBOM
        print("正在生成SBOM...")
        # 使用 subprocess.run 来执行命令，并捕获输出（注意设置 text=True 得到字符串输出）
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

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
    
        
