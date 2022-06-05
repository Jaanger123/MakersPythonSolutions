x = 'Я глобальная переменная!'
print(x)

def my_func():
    global x
    x = 'Я могу изменяться'
    
my_func()
<<<<<<< HEAD

=======
>>>>>>> 96d85f84477fbda7b8c52fb371d9ebc3c73ef002
print(x)
print(globals())