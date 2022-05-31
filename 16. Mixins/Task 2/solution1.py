class RadioMixin:
    def play_music(self, title):
        return f"Песня называется {title}"

class Auto(RadioMixin):
    pass

class Boat(RadioMixin):
    pass

class Amphibian(Auto, Boat):
    pass

obj = Amphibian() 
print(obj.play_music('Call out my name'))