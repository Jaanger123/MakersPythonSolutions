list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
new_list = ['shorter' if len(x) <= 4 else 'longer' for x in list_name ]
print(new_list)