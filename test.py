# test_yaml.py
import yaml

yaml_file = '/home/BrightSkills/Auto-Blueprints/yolov5/blueprints.yaml'

with open(yaml_file, 'r') as file:
    content = yaml.load(file, Loader=yaml.FullLoader)
    print(content)
