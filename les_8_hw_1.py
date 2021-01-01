class Data:
    data = []
    day = 0
    month = 0
    year = 0
    i = -1

    def __init__(self, birthday):
        self.birthday = birthday
        Data.data.append(self.birthday)
        Data.i += 1

    @classmethod
    def return_data(cls):
        int_list = str(cls.data[cls.i]).split('-')
        cls.day = int(int_list[0])
        cls.month = int(int_list[1])
        cls.year = int(int_list[2])

    @staticmethod
    def check_data():
        if 0 < Data.day <= 31 and 0 < Data.month <= 12 and 1900 < Data.year <= 2021:
            print('Формат даты указан верно')
        else:
            print('Формат даты указан неверно')

    def __str__(self):
        return f'День: {Data.day}, месяц: {Data.month}, год: {Data.year}'


my_birthday = Data('03-01-1996')
Data.return_data()
print(my_birthday)
Data.check_data()
your_birthday = Data('33-13-645')
Data.return_data()
print(your_birthday)
Data.check_data()