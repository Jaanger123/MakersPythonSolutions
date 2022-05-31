with open('task5.txt') as f:
    list_ = [int(i) for i in f]
    open('task6.txt','w').write(f"{min(list_)}-{max(list_)}")