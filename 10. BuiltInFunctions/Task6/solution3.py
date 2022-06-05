list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni']

temp = map(lambda word: word if len(word) > 7 else None, list_)
result = list(filter(lambda word: word, temp))

print(result)