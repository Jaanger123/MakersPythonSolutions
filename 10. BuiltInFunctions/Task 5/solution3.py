list_ = [1, 2, 3, 4] 

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

result = list(filter(is_even, list_))

print(result)