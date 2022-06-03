import math
class Math:

    def __init__(self, value) -> None:
        self.value = value
    
    def get_factorial(self):
        x = math.factorial(self.value)
        return x


    def get_sum(self):
        stri = list(map(int, str(self.value)))
        a = sum(stri)
        return a


    def get_mul_table(self):
        res2 = ''
        list1 = list(range(1, 11))
        for x in list1:
            mult = self.value * x
            res2 += f'{self.value}x{x}={mult}\n'
        return res2

num = Math(11)
print(num.get_factorial())
print(num.get_sum())
print(num.get_mul_table())
