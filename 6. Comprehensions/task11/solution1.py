a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
dict_ = {k: list(range(1,v + 1)) for k, v in a.items() }
print(dict_)