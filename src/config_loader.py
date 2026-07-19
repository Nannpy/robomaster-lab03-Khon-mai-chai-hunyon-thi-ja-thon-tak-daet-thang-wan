import yaml
import os

def load_settings():
    # A function to read data from settings.yaml and return it as a dictionary
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, '..', 'config', 'settings.yaml')
    
    with open(config_path, 'r') as file:
        settings = yaml.safe_load(file)
    return settings