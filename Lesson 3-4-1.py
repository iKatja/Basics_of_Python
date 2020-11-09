def my_func(x, y):
    try:
        y = int(y)
        if y >= 0:
            return 'Степень должна быть целым отрицательным числом'
        z = round(1 / (x ** abs(y)), 4)
        return z
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'


print(my_func(2, -2))
