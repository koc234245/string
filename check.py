product_name = input('Введите наименование товара: ')
product_quantity = input('Введите количество товара: ')
product_price = input('Введите цену товара: ')
product_totalprice = int(product_quantity) * int(product_price)
print('Итоговая цена:', product_totalprice)
deposit = input('Введите внесённую сумму: ')
change =  int(deposit) - int(product_totalprice)
print('==============Чек=============',
'\nТовар:','{:>23}'.format(product_name),
    '\nЦена:', '{:>24}'.format(product_quantity + 'кг' + " * " + product_price + 'тг/кг'),
        '\nИтого:', '{:>23}'.format(str(product_totalprice) + 'тг'), 
            '\nВнесенная сумма:', '{:>13}'.format(deposit + 'тг'),
    '\nСдача:', '{:>23}'.format(str(change) + 'тг'), 
 '\n==============================')