class Nobel:
    def __init__(self,category,year,winner):
        self.category = category
        self.year = year
        self.winner = winner

    def get_year(self):
        import datetime
        present = int(datetime.datetime.now().year)
        res = present - self.year
        return f"выиграл {res} лет назад"


winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
print(winner1.category, winner1.year,winner1.winner ) 
print(winner1.get_year())

  
winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
print(winner2.category, winner2.year,winner2.winner) 
print(winner2.get_year())