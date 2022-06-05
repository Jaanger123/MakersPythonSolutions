class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name:{self.name}, age:{self.age}")

class Student(Person):
    def __init__(self, name, age, faculty):
        Person.__init__(self, name, age)
        self.faculty = faculty

    def display_student(self):
        print(f"name:{self.name}, age:{self.age}, faculty:{self.faculty}")

obj_student = Student("Rick", 21, "science")
obj_student.display() 
obj_student.display_student()