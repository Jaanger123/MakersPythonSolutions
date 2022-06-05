def foo():
    global var
    var = 'переменная foo'

    def bar():
        global var
        print(f'переменная в foo:  {var}')
        var = 'переменная bar'

    bar()
foo()
<<<<<<< HEAD
print("переменная в foo: ", var)


=======
print("переменная в foo: ", var)
>>>>>>> 96d85f84477fbda7b8c52fb371d9ebc3c73ef002
