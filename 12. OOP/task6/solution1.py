class Salary:
    percent = 8
    def __init__(self, salary, experience):
        self.salary = salary
        self.experience = experience

    def count_percent(self):
        b = self.salary * (Salary.percent * 0.01)
        return self.experience * b

obj = Salary(10000, 10)
print(obj.count_percent())
