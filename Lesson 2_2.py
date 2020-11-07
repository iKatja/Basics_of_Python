num = abs(int(input('Введите количество элементов списка')))
new_list = []
i = 0
j = 0
while i < num:
    new_list.append(input('Введите новый элемент списка'))
    i += 1

if len(new_list) % 2 == 0:
    while j < len(new_list):
        el = new_list[j]
        new_list[j] = new_list[j + 1]
        new_list[j + 1] = el
        j += 2
else:
    while j < len(new_list) - 1:
        el = new_list[j]
        new_list[j] = new_list[j + 1]
        new_list[j + 1] = el
        j += 2

print(new_list)