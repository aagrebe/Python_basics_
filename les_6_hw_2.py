class Road():
    weight = 25
    depth = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        self.mass = self._length * self._width * Road.weight * Road.depth
        return self.mass

    def print_mass(self):
        print(f'Масса покрываемого дорожного полотна: {round(self.mass/1000)}т.')

length = int(input("Введите длину дороги в метрах, покрываемой асфальтом: "))
width = int(input("Введите ширину дороги в метрах: "))
r = Road(length, width)
print(f'По умолчанию задана масса асфальта (для 1 кв.м. на 1 см.) - {r.weight}кг. и толщина полотна - {r.depth}см.')
r.mass()
r.print_mass()