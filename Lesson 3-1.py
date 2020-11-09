def my_f(arg1, arg2):
    try:
        arg1 = int(input('Введите делимое'))
        arg2 = int(input('Введите делитель'))
        result = arg1 / arg2
    except ValueError:
        return 'Неверный формат!'
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'
    return result


print(my_f(4, 2))