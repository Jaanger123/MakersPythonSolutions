class ExtensionMixin:
    def add_extension(self, extension):
        self.extensions += [extension]
        return 'Добавлено новое расширение {} для игры {}'.format(extension, self.name)
    
    def remove_extension(self, extension):
        if extension in self.extensions:
            index = self.extensions.index(extension)
            self.extensions.pop(index)
            return '{} был отключен от {}'.format(extension, self.name)
        else:
            return 'Такого расширения нет в списке.'

class Game(ExtensionMixin):
    def __init__(self, name, type):
        self.type = type
        self.name = name
        self.extensions = []

    def get_description(self, desc):
        return '{} это {}'.format(self.name, desc)

    def get_extensions(self):
        return self.extensions if self.extensions else 'Нет подключенных расширений'

game = Game(10, 'Minecraft')

print(game.get_description('инди-игра в жанре песочницы с элементами выживания и открытым миром.'))
print(game.add_extension('Multiverse-Core'))
print(game.get_extensions())