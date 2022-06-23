inp1 = input()

try:
    list_ = []
    data = inp1.split()
    for number in data:
        list_.append(int(number))
    print(list_)
except:
    raise TypeError('Данный элемент не является числом!')