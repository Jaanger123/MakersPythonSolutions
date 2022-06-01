from functools import reduce

list_ = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, list_)
print(result)

# можно так но платформа не принимает т.к. нужен именно built-in func т.е. sum()
# в общем все solutions кроме solution1.py платформа не принимает