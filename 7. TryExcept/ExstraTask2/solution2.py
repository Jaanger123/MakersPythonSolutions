inp1 = input()
try:
    list_ = []
    list1 = inp1.split()
    for i in list1:
        list_.append(int(i))
    print(list_)
except:
    raise TypeError('Данный элемент не является числом!')