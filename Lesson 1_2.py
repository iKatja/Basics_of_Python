sec = int(input('Введите время в секундах'))
hour = sec // 3600
minute = (sec % 3600) // 60
last_sec = (sec % 3600) % 60
print(f"Время в формате чч:мм:сс   {hour} : {minute} : {last_sec}")

