inp1 = input()
try:
    list_ = [int(i) for i in list(inp1.split())]
    print(list_)
except:
    raise TypeError('Данный элемент не является числом!')