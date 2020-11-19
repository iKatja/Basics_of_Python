''' Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''
def summary():
    try:
        with open('test_5.txt', 'w+') as file_obj:
            data = input('Введите числа, разделенные пробелами \n')
            file_obj.writelines(data)
            group = data.split()
            print(sum(map(int, group)))
    except ValueError:
        print('Неверный формат числа!')
summary()

