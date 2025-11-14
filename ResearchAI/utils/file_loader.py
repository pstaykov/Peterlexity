import os
import json

def load_json(filename):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # ResearchAI/
    filepath = os.path.join(base_dir, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
