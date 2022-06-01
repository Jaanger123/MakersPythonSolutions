def multiply_list(list_):
    product = 1
    for i in list_:
        product *= i
    return product
print(multiply_list([1, 2, 3, 4, 5, 6]))