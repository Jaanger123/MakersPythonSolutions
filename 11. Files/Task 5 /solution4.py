f = open('task5.txt')
list_ = [int(i) for i in f]
f_ = open('task6.txt','w')
f_.write(f"{min(list_)}-{max(list_)}")
f.close()
f_.close()