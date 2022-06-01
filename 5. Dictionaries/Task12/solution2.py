a = {'apple': 2, 'orange': 5, 'banana': 10}

for k, v in list(a.items()):
    if v % 2 == 0:
        del a[k]
        
print(a)