'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class ByNull:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def by_null(x, y):
        try:
            return x / y
        except:
            return f"Делить на ноль нельзя"


div = ByNull(10, 100)
print(ByNull.by_null(10, 0))
print(ByNull.by_null(10, 0.1))
print(div.by_null(100, 0))
