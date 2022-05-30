def divide(arg1=int, arg2=int):
    result = divmod(arg1,arg2)
    return result[0]

print(divide(5.2,3))