import os
import json

def read_config():
    with open("config.json", "r") as f:
        config = json.load(f)
    f.close()
    return config