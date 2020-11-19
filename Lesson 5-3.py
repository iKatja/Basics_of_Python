'''Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.'''
my_data = {'Harry Potter': 30000, 'Ron Weasley': 19000, 'Hermione Granger': 29000, 'Draco Malfoy': 15000}
f = open('test_3.txt', 'w')
for name, salary in my_data.items():
    f.write(name + ':' + str(salary) + '\n')
f.close()
sum = 0
count = 0
persons = []
with open('test_3.txt', 'r') as file_obj:
    for line in file_obj:
        print(line, end='')
        parts = line.split(':')
        if int(parts[1]) < 20000:
            persons.append(parts[0])
        sum += int(parts[1])
        count += 1
    result = sum / count
print(f'Сотрудники с ЗП меньше 20 тысяч: {persons}')
print(f'Средний доход: {result}')
