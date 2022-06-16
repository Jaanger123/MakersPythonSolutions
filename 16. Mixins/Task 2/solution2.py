class RadioMixin:
    @classmethod
    def play_music(cls, title):
        return 'Песня называется ' + title

class Auto(RadioMixin):
    pass

class Boat(RadioMixin):
    pass

class Amphibian(Auto, Boat):
    pass

auto = Auto()
boat = Boat()
obj = Amphibian()

print(auto.play_music('Die for you'))
print(boat.play_music('Die for you'))
print(obj.play_music('Die for you'))