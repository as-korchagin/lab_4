from lab_4.librip.gens import field
from lab_4.librip.gens import gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1


get_gen_random = gen_random(1, 50, 9)
get_field = field(goods, 'title', 'price')
print(", ".join(map(str, get_gen_random)) + ' ' + ", ".join(map(str, get_field)))
