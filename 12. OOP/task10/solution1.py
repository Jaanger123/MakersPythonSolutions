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
