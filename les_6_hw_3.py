class Worker():
    def __init__(self, name, surname, patronymic, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.position = position
        self._income = {'wage': wage,
                        'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'Ф.И.О.: {self.surname} {self.name} {self.patronymic}')

    def get_total_income(self):
        self.sum_income = sum(self._income.values())
        print(f'Суммарный доход: {self.sum_income} рублей')


p = Position("Геннадий", "Иванов", "Сергеевич", "Сантехник", 30000, 15000)
p.get_full_name()
print(p.position)
p.get_total_income()