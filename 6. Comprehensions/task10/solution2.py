n = int(input())
dict_ = {x:x*x for x in range(1, 501) if x % n == 0}
print(dict_)