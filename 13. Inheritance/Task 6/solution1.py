class ContactList(list):
    def __init__(self,arg=list):
        self.arg = arg

    def search_by_name(self,name):
        result = [x for x in self.arg if name in x]
        return result

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya')) 