goods = []
item = 1
while True:
    check = input('Для выхода нажмите "В", для добавления товара нажмите "Т", для получения аналитики нажмите "А"').upper()
    if check == 'В':
        print('До встречи!')
        break
    if check == 'Т':
        attribute = {'название': input('Введите наименование товара'), 'цена': float(input('Введите цену товара')),
                     'количество': float(input('Введите количество товара')),
                     'ед.': input('Введите единицу измерения товара')}
        goods.append(tuple([item, attribute]))
        item += 1
        print(goods)
    if check == 'А':
        data = {'название': [],
                'цена': [],
                'количество': [],
                'ед.': []}
        for _, item in goods:
            data['название'].append(item['название'])
            data['цена'].append(item['цена'])
            data['количество'].append(item['количество'])
            data['ед.'].append(item['ед.'])
        print(data)


