num = abs(int(input('Введите целое положительное число')))
a = num % 10
num = num // 10
while num > 0:
    if num % 10 > a:
        a = num % 10
    num = num // 10
print('Максимальная цифра в числе равна', a)