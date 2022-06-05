list_ = [1, 5, -9, 6, -4]

def func(ls):
    new_list = []
    for num in ls:
        if num > 3:
            new_list.append(num)
        else:
            pass

    if len(new_list) < len(ls):
        return False
    else:
        return True

print(func(list_))