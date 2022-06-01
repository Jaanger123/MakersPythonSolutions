import json
f = open('task1.json')
python_obj = json.load(f)
f.close()
f_ = open('task1.py', 'w')
f_.write(str(python_obj))
f_.close()