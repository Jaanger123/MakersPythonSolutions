class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_info(self):
        return 'Привет, меня зовут {} {}'.format(self.name, self.last_name)

class Employee(Person):
    def __init__(self, name, last_name, work, status):
        Person.__init__(self, name, last_name)
        self.work = work
        self.status = status

    def get_info(self):
        person_info = Person.get_info(self)
        return '{}, я работаю в компании {} на должности {}'.format(person_info, self.work, self.status)

class Student(Person):
    def __init__(self, name, last_name, university, course):
        Person.__init__(self, name, last_name)
        self.university = university
        self.course = course

    def get_info(self):
        person_info = Person.get_info(self)
        return '{}, я учусь в {} на {} курсе'.format(person_info, self.university, self.course)


person = Person('Иван', 'Петров')
employee = Employee('Иван', 'Петров', 'компании Рога и копыта', 'директор')
student = Student('Иван', 'Петров', 'КГТУ', '3 курсе')

def get_human_info(obj):
    print(obj.get_info())

get_human_info(employee) 
get_human_info(student) 
get_human_info(person)