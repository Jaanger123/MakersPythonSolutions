a = {'a': 1, 'b': 2, 'c': 1}
b = a.copy()

for key in b:
    print(a.pop(key))