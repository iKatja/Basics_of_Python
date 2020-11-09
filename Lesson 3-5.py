def my_sum():
    sum_res = 0
    i = 1
    while i == 1:
        number = input('Введите числа, разделенные пробелом / Для выхода нажмите Q: ').upper().split(" ")
        res = 0
        for el in range(len(number)):
            if number[el] == 'Q':
                print('Программа завершена')
                i = 0
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма равна {sum_res}')

my_sum()