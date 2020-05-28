start = {'m': 'Дорогой',
         'f': 'Дорогая'
         }

person = [
         ['Семен', 'Семенович', 123.5, 'm'],
         ['Иван', 'Иванович', 23.4, 'm'],
         ['Антон', 'Антонович', 65.8, 'm'],
         ['Алла', 'Алловна', 12.65, 'f']
]

for name, lastname, balance, gender in person:
    message = f'{start[gender]} {name} {lastname}, на вашем счету отсталось {balance} грн.'
    print(message)
