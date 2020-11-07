user_str = input('Введите строку из нескольких слов, разделённых пробелами')
my_str = user_str.split(' ')
for i, el in enumerate(my_str, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")
