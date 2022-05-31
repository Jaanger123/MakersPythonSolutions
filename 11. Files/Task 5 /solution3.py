f = open('task5.txt')
list_ = []
for i in f:
    list_.append(int(i))
f_ = open('task6.txt', 'w')
print(f_.write(f"{min(list_)}-{max(list_)}"))
f.close()
f_.close()