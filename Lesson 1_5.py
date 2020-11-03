earn = int(input('Введите значение выручки'))
cost = int(input('Введите значение издержек'))
finrez = earn - cost
rent = finrez / earn * 100
if finrez > 0:
    print('Вы получили прибыль', finrez, 'денежных единиц. Рентабельность выручки составила', rent, '%')
    numbers = int(input('Введите численность сотрудников'))
    finnum = finrez / numbers
    print('Прибыль на одного сотрудника составила', finnum, 'денежных единиц.')
elif finrez == 0:
    print('Вы отработали в ноль')
else:
    print('Вы получили убыток', finrez, 'денежных единиц.')
