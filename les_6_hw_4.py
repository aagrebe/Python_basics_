class Car():
    car_counter = 0
    car_list = []

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        Car.car_counter += 1

    def item_car_list(self):
        el = {'скорость': self.speed,
              'цвет': self.color,
              'марка': self.name,
              'категория полиции': self.is_police}
        self.car_list.append(el)

    def go(self):
        return f'Машина поехала'

    def stop(self):
        return f'Машина остановилась'

    def turn(self, direction):
        if direction == "r":
            return f'Машина повернула направо'
        elif direction == "l":
            return f'Машина повернула налево'
        elif direction == "s":
            return f'Машина поехала прямо'
        elif direction == "b":
            return f'Машина поехала назад'
        else:
            return f'Неверно указано направление'

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость автомобиля: {self.speed} км/ч. Вы превышаете скорость!')
        else:
            print(f"Текущая скорость автомобиля: {self.speed} км/ч")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость автомобиля: {self.speed} км/ч. Вы превышаете скорость!')
        else:
            print(f"Текущая скорость автомобиля: {self.speed} км/ч")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name)
        self.is_police = True


town_car = TownCar(70, 'red', 'Volkswagen')
town_car.item_car_list()
print(Car.car_list[0])
town_car.show_speed()
print(f'{town_car.go()}/{town_car.turn("l")}/{town_car.stop()}')
sport_car = SportCar(223, 'orange', 'Ferrari')
sport_car.item_car_list()
print(Car.car_list[1])
sport_car.show_speed()
print(f'{sport_car.go()}/{sport_car.turn("r")}/{sport_car.stop()}')
worker_car = WorkCar(55, 'grey', 'Honda')
worker_car.item_car_list()
print((Car.car_list[2]))
worker_car.show_speed()
print(f'{worker_car.go()}/{worker_car.turn("s")}/{worker_car.stop()}')
police_car = PoliceCar(102, 'white', 'Ford')
police_car.item_car_list()
print((Car.car_list[3]))
print(f'{police_car.go()}/{police_car.turn("b")}/{police_car.stop()}')
print(f'Итого машин: {Car.car_counter}')
