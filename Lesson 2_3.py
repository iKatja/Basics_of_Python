list_seasons = ['зима', 'весна', 'лето', 'осень']
dict_months = {
    0: 'зима',
    1: 'весна',
    2: 'лето',
    3: 'осень',
}
month = abs(int(input('Введите номер месяца')))

if month == 1 or month == 2 or month == 12:
    print('Это', list_seasons[0])
    print('Это', dict_months.get(0))
elif month == 3 or month == 4 or month == 5:
    print('Это', list_seasons[1])
    print('Это', dict_months.get(1))
elif month == 6 or month == 7 or month == 8:
    print('Это', list_seasons[2])
    print('Это', dict_months.get(2))
elif month == 9 or month == 10 or month == 11:
    print('Это', list_seasons[3])
    print('Это', dict_months.get(3))
else:
    print('На этой планете всего 12 месяцев!')