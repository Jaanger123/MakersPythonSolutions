list_ = [-1, 2, 3, 5, -3, 7]

def is_gt(num):
    if num > 0:
        return True
    return False

result = list(map(is_gt, list_))

print(result)