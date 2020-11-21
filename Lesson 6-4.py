'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.'''


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'\nМашина {self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} едет {direction}.'

    def show_speed(self):
        return f'\nВаша текущая скорость {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы превысили скорость! Ваша текущая скорость {self.speed} км/ч'
        else:
            return f'\nВаша текущая скорость {self.speed} км/ч'



class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превысили скорость! Ваша текущая скорость {self.speed} км/ч'
        else:
            return f'\nВаша текущая скорость {self.speed} км/ч'


class PoliceCar(Car):
    pass


town = TownCar(80, 'grey', 'MB', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('влево'), town.turn('вправо'), town.stop())

sport = SportCar(180, 'blue', 'MB AMG', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('влево'), sport.turn('вправо'), sport.stop())

work = WorkCar(60, 'green', 'Ford', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('влево'), work.turn('вправо'), work.stop())

police = PoliceCar(90, 'white-blue', 'Ford', True)
print('3:\n' + police.go(), police.show_speed(), police.turn('влево'), police.turn('вправо'), police.stop())