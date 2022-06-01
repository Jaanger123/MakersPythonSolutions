import json
with open('task2.json') as f:
    json_obj = f.read()
    python_obj = json.loads(json_obj)
