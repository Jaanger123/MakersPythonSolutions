dict_ = {'key1': 'value1', 'key2': 'value2'}
try:
    print(dict_['key3'])
except KeyError:
    print('Нет такого ключа!')