class CustomError(Exception):
    def __init__(self,name):
        self.name = name
capitals_error = CustomError("ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ")

def check_letters(string):
    if string.isupper():
        return f'ВСЕ ОТЛИЧНО! {string}'
    else:
        raise capitals_error

print(check_letters("HELLO"))