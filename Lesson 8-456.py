'''Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''


class Store:
    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def to_take(self):
        try:
            i = input(f'Введите наименование')
            i_price = int(input(f'Введите цену'))
            i_quantity = int(input(f'Введите количество'))
            unit = {'Модель устройства': i, 'Цена за ед': i_price, 'Количество': i_quantity}
            self.my_unit.update(unit)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'


class Printer(Store):
    def __init__(self, name, price, quantity, color=False):
        super().__init__(name, price, quantity)
        self.color = color


class Scan(Store):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size


class Copy(Store):
    def __init__(self, name, price, quantity, repeat):
        super().__init__(name, price, quantity)
        self.repeat = repeat


unit_1 = Printer('Brother', 3500, 5, True)
unit_2 = Scan('Canon', 1800, 5, 'big')
unit_3 = Copy('Xerox', 1500, 8, True)
print(unit_1.to_take())
print(unit_2.to_take())
print(unit_3.to_take())
