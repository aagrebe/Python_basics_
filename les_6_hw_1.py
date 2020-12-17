import time

class TrafficLight():
    def __init__(self):
        self.__color = "красный"

    def traffic_color(self):
        for el in range(2):
            print(f'Цвет светафора - {self.__color}. Цвет светафора поменяется на желтый через 7 секунд')
            time.sleep(7)
            self.__color = "желтый"
            print(f'Цвет светафора - {self.__color}. Цвет светафора поменяется на зеленый через 2 секунды')
            time.sleep(2)
            self.__color = "зелeный"
            print(f'Цвет светафора - {self.__color}. Цвет светафора поменяется на красный через 9 секунд')
            time.sleep(9)
            self.__color = "красный"


light = TrafficLight()
light.traffic_color()