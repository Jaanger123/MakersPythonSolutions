with open("task3.txt", "w")as file1:
    for x in range(10):
        list_ =  (str(x) + "*")
        file1.write(list_)
    file1.seek(0)
with open('task3.txt', 'r') as file2:
    print(file2.read())