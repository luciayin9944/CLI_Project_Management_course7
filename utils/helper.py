import json
import os

# Ensure the data directory exists
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

def get_data_path(filename):
    """Returns the full path of a file inside the data/ directory"""
    return os.path.join(DATA_DIR, filename)

def save_json(filename, data):
    """Saves JSON data to the data/ folder"""
    full_path = get_data_path(filename)
    with open(full_path, 'w') as f:
        json.dump(data, f, indent=2)

def load_json(filename):
    """Loads JSON data from the data/ folder"""
    full_path = get_data_path(filename)
    if os.path.exists(full_path):
        with open(full_path) as f:
            return json.load(f)
    return []


# def save_json(filename, data):
#     with open(filename, 'w') as f:
#         json.dump(data, f, indent=2)

# def load_json(filename):
#     if os.path.exists(filename):
#         with open(filename) as f:
#             return json.load(f)
#     return []
