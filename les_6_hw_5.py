class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print(f'Для отрисовки используется {self.title}')
class Pencil(Stationery):
    def draw(self):
        print(f'Для отрисовки используется {self.title}')
class Handle(Stationery):
    def draw(self):
        print(f'Для отрисовки используется {self.title}')


tool = Stationery('канцелярская принадлежность')
tool.draw()
tool_pen = Pen('ручка')
tool_pen.draw()
tool_pencil = Pencil('карандаш')
tool_pencil.draw()
tool_handle = Handle('маркер')
tool_handle.draw()