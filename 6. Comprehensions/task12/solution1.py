dict_ = {'first': 1, 'second': 2, 'third': 3} 
a = {k: 'even' if v % 2 == 0 else 'odd' for k, v in dict_.items()}
print(a)