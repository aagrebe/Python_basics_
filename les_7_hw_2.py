from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    s = 0

    @abstractmethod
    def add_brand(self):
        pass

    @abstractmethod
    def material(self):
        pass

    @property
    def all_sum(self):
        AbstractClothes.s += self.n_material
        return round(AbstractClothes.s, 2)

class Coat(AbstractClothes):
    def __init__(self, V, name='пальто'):  # V - размер
        self.V = V
        self.name = name

    def add_brand(self):
        self.brand = input('Введите бренд пальто: ')
        return self.brand

    def material(self):
        self.n_material = self.V / 6.5 + 0.5
        return round(self.n_material, 2)

    @property
    def print_info(self):
        return f'Информация о товаре: категория {self.name}, бренд {self.brand}, размер {self.V}'


class Suit(AbstractClothes):
    def __init__(self, H, name='костюм'):  # H - рост
        self.H = H
        self.name = name

    def add_brand(self):
        self.brand = input('Введите бренд костюма: ')
        return self.brand

    def material(self):
        self.n_material = 2 * self.H + 0.3
        return round(self.n_material, 2)

    @property
    def print_info(self):
        return f'Информация о товаре: категория {self.name}, бренд {self.brand}, рост {self.H} м.'


c = Coat(22)
s = Suit(1.9)
c.add_brand()
s.add_brand()
print(c.print_info)
print(s.print_info)
print(f'Расход ткани на пальто: {c.material()} м.')
print(f'Расход ткани на костюм: {s.material()} м.')
c.all_sum
print(f'Общий расход ткани: {s.all_sum} м.')