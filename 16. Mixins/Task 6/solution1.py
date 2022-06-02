class Todo:
    def __init__(self):
        todos = {}

    def set_deadline(self,time):
        time
        from datetime import datetime
        a = datetime.now().strftimestrftime("%H:%:%S")

def set_deadline(time_):
    from datetime import datetime
    res = datetime.strptime(time_, '%Y/%m/%d')
    print(res)
    a = datetime.today()
    print(str(a - res).split(',')[0])
set_deadline("2021/12/31")

class CreateMixin:
    def create(self, key, todo):
        if key in self.todos.keys():
            return 'Задача под таким ключём уже существует'
        self.todos[key] = todo
        return self.todos
class DeleteMixin:
    def delete(self, key):
        if key in self.todos.keys():
            res = self.todos.pop(key)
        return res
class UpdateMixin:
    def update(self, key, new_value):
        self.todos.update({key:new_value})
        return self.todos
class ReadMixin:
    def read(self):
        res = [x for x in self.todos.items()]
        return sorted(res)
class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    def __init__(self):
        self.todos = {}
    def set_deadline(self, data):
        from datetime import date
        data = data.split('/')
        dead_line = date(int(data[2]), int(data[1]),int(data[0]))
        date_now = date.today()
        res = dead_line- date_now
        return res.days

task = ToDo()
print(task.create(1, 'Do housework'))
print(task.create(1, 'Do housework'))
print(task.create(2,'Go for a walk'))
print(task.update(1, 'Do homework'))
print(task.delete(2))
print(task.read())
print(task.set_deadline('31/12/2021'))