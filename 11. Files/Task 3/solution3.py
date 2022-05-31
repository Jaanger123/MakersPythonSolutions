file_ = open("task3.txt", "w+")
for x in range(10):
    list_ =  (str(x) + "*")
    file_.write(list_)
file_.seek(0)
print(file_.read())
file_.close()