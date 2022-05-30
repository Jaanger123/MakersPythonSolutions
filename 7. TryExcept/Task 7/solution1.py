try:
    age = int(input())
    if age < 18:
        raise ValueError('Доступ запрещён')
except ValueError:
    print('Введён некорректный возраст\n')
else:
    print('Спасибо')
finally:
    print('До свидания!')