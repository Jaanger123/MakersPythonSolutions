# a = {'a': 10, 'b': 9, 'c': 3}
# result = 1
# for key in a:    
#     result = result * a[key]
# print(result)

import math
d = {'a': 10, 'b': 9, 'c': 3}
result = math.prod(d.values())
print(result)