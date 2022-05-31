class ToDo:
    instances = {}
    def __init__(self, prior1):
        self.prior1 = prior1
    
    def give_priority(self, priority):
        ToDo.instances[priority] = self.prior1


    def list_of_tasks(self):
        list_ = []
        for key, value in ToDo.instances.items():
            list_.append(tuple([key,value]))
        return sorted(list_)

prior1 = ToDo('сделать домашку')
prior1.give_priority(1)
prior2 = ToDo('сходить в кино')
prior2.give_priority(2)
prior3 = ToDo('выгулять собаку')
prior2.give_priority(3)
print(ToDo.instances)
print(prior1.list_of_tasks())

class Spam:
    val = 1

    def __init__(self, n):
        val = 5

obj = Spam(5)
print(obj.val)

class Nums:
    def __init__(self, num):
        self.num = num
        print(f'1000 - {self.num}')

Nums('7')


class A:
    def __init__(self) -> None:
        self.a = 0

    def change(self,n):

        a = n

obj = A()
obj.change(2)
print(obj.a)
