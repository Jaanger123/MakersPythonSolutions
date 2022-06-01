def count_symbols(str):
    count = 0
    count1 = 0
    count2 = 0
    
    for x in str.lower():
        if x in "йуеыаоэяиюё":
            count += 1 
        elif x in "цкнгшщзмчвфжрлдтсп":
            count1 += 1
        else:
            count2 += 1
    return f'Количество гласных: {count}, согласных: {count1}, остальных символов: {count2}'

print(count_symbols('Мурат супер'))