list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni']

is_gt = lambda word: len(word) > 7
result = list(filter(is_gt, list_))

print(result)