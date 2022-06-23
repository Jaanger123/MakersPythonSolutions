inp1 = input()

try:
    list_ = [int(num) for num in list(inp1.split())]
    print(list_)
except:
    raise TypeError('Данный элемент не является числом!')