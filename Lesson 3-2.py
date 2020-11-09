name = input('Введите имя')
surname = input('Введите фамилию')
year = input('Введите год рождения')
city = input('Введите город проживания')
email = input('Введите email')
phone = input('Введите телефон')


def my_f(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])


print(my_f(name='Катя', surname='Захарова', year='1979', city='Москва', email='default@gmail.com', phone='911'))