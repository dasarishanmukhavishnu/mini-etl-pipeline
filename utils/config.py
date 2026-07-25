import yaml
import os

def load_config(file_path: str) -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File path: {file_path} doesn't exists...\nPlease check path: {file_path}")
    
    with open(file_path,'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise RuntimeError(f"While running yaml file occured an error: {e}")
            