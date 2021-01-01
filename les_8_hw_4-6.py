class Office_equipment(): #оргтехника

    technic_counter = 0
    technic_dict = {}
    locations_of_company = set()

    def __init__(self, name, number, price, location):
        self.name = name
        self.number = number
        self.price = price
        self.location = location
        self.paper = True
        Office_equipment.technic_counter += 1
        Office_equipment.technic_dict[name] = [number, price]
        Office_equipment.locations_of_company.add(location)

class Warehouse: #склад
    def __init__(self):
        self.items = []
        self.analytics = {'names': [],
                          'amount': [],
                          'money': 0}

    def add_item(self, name, number, price):
        el = {'наименование': name,
              'количество': number,
              'стоимость': price}

        self.items.append(el)
        self.analytics['names'].append(name)
        self.analytics['amount'].append(number)
        self.analytics['money'] += price

    def __str__(self):
        return f'{self.items}' \
               f'{self.analytics}'

class Printer(Office_equipment, Warehouse): #принтер
    pass

class Scanner(Office_equipment): #сканнер
    pass

class Copier(Office_equipment): #ксерокс

    pass


p = Printer('принтер', 5, 2000, 'корридор')
s = Scanner('сканер', 3, 5000, 'офис')
с = Copier('ксерокс', 4, 3000, 'ресепшн')


print(Office_equipment.technic_counter)
print(Office_equipment.technic_dict)
print(Office_equipment.locations_of_company)