with open('task5.txt') as f:
    list_ = []
    for i in f:
        list_.append(int(i))

    with open('task6.txt', 'w') as f_:
        f_.write(f"{min(list_)}-{max(list_)}")