list_ = [-1, 2, 3, 5, -3, 7]

temp = [0 if num <= 0 else 1 for num in list_]
result = list(map(lambda num: bool(num), temp))

print(result)