string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
list_ = [x for x in string_.split() if x.isdecimal()]
print(list_)