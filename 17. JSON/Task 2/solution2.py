import json
f = open('task2.json')
json_obj = f.read()
f.close()
python_obj = json.loads(json_obj)
