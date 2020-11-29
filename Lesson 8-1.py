'''Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_list = []
        for i in day_month_year.split():
            if i != '-':
                my_list.append(i)
        return int(my_list[0]), int(my_list[1]), int(my_list[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Проверка завершена, всё в порядке!'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


today = Data('29 - 11 - 2020')
print(Data.valid(31, 11, 2023))
print(today.valid(13, 13, 2013))
print(Data.extract('29 - 11 - 2020'))
print(today.extract('29 - 11 - 2020'))