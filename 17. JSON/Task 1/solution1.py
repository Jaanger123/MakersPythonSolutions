import json
with open('task1.json') as f:
    python_obj = json.load(f)
    f_ = open('task1.py', 'w')
    f_.write(str(python_obj))
    f_.close()