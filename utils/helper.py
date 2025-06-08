import json
import os


def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_json(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            return json.load(f)
    return []
