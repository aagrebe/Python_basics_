class Office_equipment:  # оргтехника
    technic_counter = 0
    technic_dict = {}

    def __init__(self, name, number, price, location):
        self.name = name
        self.number = number
        self.price = price
        self.location = location
        Office_equipment.technic_counter += 1
        Office_equipment.technic_dict[name] = [number, price]

    @classmethod
    def check_data(cls, technic):
        try:
            if str(technic.name) and int(technic.number) and int(technic.price) and str(technic.location):
                print('Данные введены верно')
        except ValueError:
            print('Данные введены неверно')


class Warehouse:  # склад
    items = []
    analytics = {'names': [],
                 'amount': [],
                 'money': 0}
    locations_of_company = set()

    def add_item(self, name, number, price, location):
        el = {'наименование': name,
              'количество': number,
              'стоимость': price}

        Warehouse.items.append(el)
        Warehouse.analytics['names'].append(name)
        Warehouse.analytics['amount'].append(number)
        Warehouse.analytics['money'] += price
        Warehouse.locations_of_company.add(location)


class Printer(Office_equipment, Warehouse):
    def __init__(self, name, number, price, location):
        super().__init__(name, number, price, location)

    def add_item(self, **kwargs):
        super().add_item(self.name, self.number, self.price, self.location)


class Scanner(Office_equipment, Warehouse):
    def add_item(self, **kwargs):
        super().add_item(self.name, self.number, self.price, self.location)


class Copier(Office_equipment, Warehouse):
    def add_item(self, **kwargs):
        super().add_item(self.name, self.number, self.price, self.location)


printer = Printer('принтер', 5, 2371, 'бухгалтерия')
Office_equipment.check_data(printer)
scan = Scanner('сканер', 3, 5155, 'отдел рекламы')
copy = Copier('ксерокс', 4, 3610, 'отдел управления')
printer.add_item()
scan.add_item()
copy.add_item()
print(f'Всего единиц оргтехники: {Office_equipment.technic_counter}')
print(f'Список оргтехники: {Office_equipment.technic_dict}')
print(f'Технику нужно разместить в следующих отделах: {Warehouse.locations_of_company}')
print(f'Информация о поступлениях: {Warehouse.items}')
print(f'Общая аналитика по складу: {Warehouse.analytics}')
