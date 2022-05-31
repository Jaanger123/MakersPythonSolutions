dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

new_dict = {key1 : [key2 for key2, value2 in value1.items() if value1[key2] == max(value1.values()) ][0]  for key1, value1 in dict_.items()}
print(new_dict)

