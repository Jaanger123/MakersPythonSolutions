dict_ = {1: 'Hello', 2: 'World', 3: 'John'}
hello = {k: len(v) if k % 2 == 0 else len(v) ** 3 for k,v in dict_.items()}
print(hello)