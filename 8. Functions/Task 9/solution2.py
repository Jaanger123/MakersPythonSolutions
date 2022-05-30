from functools import reduce

def multiply_list(list_):
    result = reduce(lambda x, y: x*y, list_)
    return result
l = [1, 2, 3, 4, 5]

print(multiply_list(l))
