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

print(f'33*44={33 * 44}')

for name, lastname, balance, gender in person:
    message = f'{name=} {lastname=} {balance=}'
    print(message)

a = 45.76589045
print(f'{a:.2f}')
b = 1234567890
print(f'{b:,}')

total = 567
part = 432
print(f'Percentage: {part / total:.2%}')
