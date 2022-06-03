set1 = {x for x in range(10)}
set2 = {y for y in range(10,20)}
full_set = set1.union(set2)
if len(full_set) < 20:
    len_ = len(full_set)
    b = set1 & set2
    print(f"В этом сете было {len(b)} повторения, его длина составляет {len_}")
elif len(full_set) == 20:
    print("Ваш объединенный сет полностью уникальный!")