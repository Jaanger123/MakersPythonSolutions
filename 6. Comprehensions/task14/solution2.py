dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

dict2 = {k : [k2 for k2, v2 in v.items() if v2 == max(v.values())][0] for k, v in dict_.items() }
print(dict2)