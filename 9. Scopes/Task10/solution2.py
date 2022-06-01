a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]

def func():
    global a
    b = ''
    for x in a:
        if x < 7:
            b += str(x)
    print(b)
func()