my_list = [7, 5, 3, 3, 2]
num = int(input('Введите новый элемент рейтинга'))
for el in range(len(my_list)):
    if num == my_list[el]:
        my_list.insert(el + 1, num)
        break
    elif num > my_list[0]:
        my_list.insert(0, num)
        break
    elif num < my_list[-1]:
        my_list.append(num)
        break
    elif num < my_list[el] and num > my_list[el + 1]:
        my_list.insert(el+1, num)
        break
print(f"Новый рейтинг: {my_list}")