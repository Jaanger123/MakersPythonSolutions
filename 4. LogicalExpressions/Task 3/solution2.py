mark = int(input())

if mark < 60:
    print('Вы не сдали экзамен')
elif mark < 70:
    print('Вам стоит подучить материал')
elif mark < 80:
    print('Хорошо, Ваша оценка 3!')
elif mark < 90:
    print('Здорово, Ваша оценка 4!')
else:
    print('Отлично, Ваша оценка 5!')

# Данное решение не сильно отличается от первого решения, но оно показывает нам что условия можно составлять по разному.