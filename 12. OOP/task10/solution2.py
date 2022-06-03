class ToDo:
    instances = {}

    def __init__(self, todo):
        self.todo = todo
    
    def give_priority(self, priority):
        self.instances[priority] = self.todo

    def list_of_tasks(self):
        return sorted(list(self.instances.items()), key=lambda todo: todo[0])

todo1 = ToDo('Сделать домашку')
todo2 = ToDo('Сходить в кино')
todo3 = ToDo('Погулять с девушкой')

todo1.give_priority(2)
todo2.give_priority(1)
todo2.give_priority(3)
print(ToDo.instances)
print(todo1.list_of_tasks())