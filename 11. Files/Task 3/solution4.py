file1 = open("task3.txt", "w")
for x in range(10):
    list_ =  (str(x) + "*")
    file1.write(list_)
file1.seek(0)
file2 = open('task3.txt', 'r')
print(file2.read())
file1.close()
file2.close()