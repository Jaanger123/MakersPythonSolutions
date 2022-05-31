my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
dict_ = {k1:[v2 for v2 in v1.values()][0] for k1, v1 in my_dict.items()}
print(dict_)