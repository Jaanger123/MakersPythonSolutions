f = open('task1.txt', 'r')
list_ = f.readlines(9)
for i in list_:
    print(i)
f.close()