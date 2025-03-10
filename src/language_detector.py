import os

def detect_language(project_path: str) -> str:
    """
    根据项目目录中的关键文件检测项目使用的语言
    """
    files = os.listdir(project_path)
    
    # 判断是否为 Python 项目
    if any(f in files for f in ['requirements.txt', 'setup.py', 'pyproject.toml']):
        return 'python'
    # 判断是否为 Go 项目
    elif 'go.mod' in files:
        return 'go'
    # 判断是否为 Java 项目
    elif any(f in files for f in ['pom.xml', 'build.gradle']):
        return 'java'
    else:
        return 'unknown'
