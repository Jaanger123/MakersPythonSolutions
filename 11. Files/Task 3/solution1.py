with open("task3.txt", "w+")as file_:
    for x in range(10):
        list_ =  (str(x) + "*")
        file_.write(list_)
    file_.seek(0)
    print(file_.read())