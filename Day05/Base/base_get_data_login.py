import yaml,os,sys

def get_data():
    with open(os.getcwd+os.sep+"Data"+os.sep+"data_login.yaml","r",encoding="utf-8") as f:
        yaml.load(f)