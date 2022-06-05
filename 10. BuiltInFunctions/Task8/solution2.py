list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = list(filter(lambda num: num % 2 == 0, list_))
list3 = list(filter(lambda num: num not in list2, list_))

result = 'even: ' + str(len(list2)) + ', odd: ' + str(len(list3))

print(result)