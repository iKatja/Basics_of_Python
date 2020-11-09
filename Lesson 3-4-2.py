def my_func(x, y):
    try:
        y = int(y)
        if y >= 0:
            return 'Степень должна быть целым отрицательным числом'
        i = -1
        z = 1
        while i >= y:
            z *= 1 / x
            i -= 1
        return z
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'


print(my_func(2, -2))
