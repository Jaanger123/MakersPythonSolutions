list_ = [1, 2, 3, 4]

def get_square(num):
    return num * num

result = list(map(get_square, list_))

print(result)