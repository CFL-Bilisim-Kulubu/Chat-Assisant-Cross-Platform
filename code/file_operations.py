import os
import json

def read_config():
    with open("config.json", "r") as f:
        config = json.load(f)
    f.close()
    return config

def read_base_prompt():
    with open("baseprompt.txt", "r") as f:
        prompt = f.read()
    f.close()
    return prompt