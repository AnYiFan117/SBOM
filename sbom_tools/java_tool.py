import os

def generate_sbom(project_path: str):
    """
    针对 Java 项目生成 SBOM。
    可通过调用 cyclonedx-maven-plugin 或其他工具实现
    """
    print(f"正在为 Java 项目 {project_path} 生成 SBOM...")
    try:
        # 在控制台进入project_path目录
        os.chdir(project_path)
        # 先安装maven
        print("正在安装maven...")
        os.system("apt-get install maven")
        # 执行SBOM生成命令：mvn org.cyclonedx:cyclonedx-maven-plugin:makeAggregateBom
        print("正在生成SBOM...")
        os.system("mvn org.cyclonedx:cyclonedx-maven-plugin:makeAggregateBom")
        print(f"SBOM生成完毕，保存在target/bom.json中")
    except Exception as e:
        print(f"SBOM生成失败：{e}")
    
