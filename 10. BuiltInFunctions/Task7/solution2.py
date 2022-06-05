from functools import reduce

list_ = [5, 6, 7, 8]

def mul(x, y):
    return x * y

result = reduce(mul, list_)

print(result)