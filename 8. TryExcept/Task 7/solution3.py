try:
    age = int(input())

    if age < 18:
        raise ValueError('Доступ запрещён')
except (ValueError, TypeError):
    print('Введён некорректный возраст')
else:
    print('Спасибо')
finally:
    print('До свидания!')