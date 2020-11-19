'''Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.'''
subjects = {}
with open('test_6.txt', 'r') as file_obj:
    lines = file_obj.readlines()
    for line in lines:
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
print(f'Общее количество занятий по предмету - \n {subjects}')