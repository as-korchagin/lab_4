import json

from librip.ctxmngrs import Timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

# path = sys.argv[1]
path = './data_light.json'
with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов


@print_result
def f1(arg):
    return list(sorted(Unique(field(arg, 'job-name'), ignore_case=False), key=lambda x: x.lower()))


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().find('программист') != -1, arg))


@print_result
def f3(arg):
    return list(map(lambda i: i + " с опытом Python", arg))


@print_result
def f4(arg):
    a = list(zip(arg, list(gen_random(100000, 200000, len(arg)))))
    return list(map(lambda i: "{}, зарплата {} руб.".format(i[0], i[1]), a))


with Timer():
    f4(f3(f2(f1(data))))
