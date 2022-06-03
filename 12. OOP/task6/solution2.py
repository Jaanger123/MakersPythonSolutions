class Salary:
    percent = 8
    def __init__(self,salary,experience):
        self.salary = salary
        self.experience = experience

    def count_percent(self):
        res = (self.salary /100 * self.percent) * self.experience
        return res

obj = Salary(12000,8)
print(obj.count_percent())