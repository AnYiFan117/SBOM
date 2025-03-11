import yaml

def load_myconfig(config_path: str):
    """
    加载 YAML 格式的配置文件
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config
