#coding=utf-8
import yaml
import os

cur=os.path.dirname(os.path.realpath(__file__))

def get_token(yamlName="token.yaml"):

    yaml_file_path = os.path.join(cur, yamlName)
    f = open(yaml_file_path)
    file_data = f.read()
    t = yaml.load(file_data)
    f.close()
    return t['token']
if __name__ =="__main__":
    get_token()