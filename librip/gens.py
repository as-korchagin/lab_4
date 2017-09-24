import random


def field(items, *args):
    assert len(args) > 0
    result = list()
    for item in items:
        if len(args) == 1 and (item.get(args[0]) is not None):
            result.append(item.get(args[0]))
        elif len(args) > 1:
            if None not in set(item.get(arg) for arg in args):
                result.append({arg: item.get(arg) for arg in args})
    return result


def gen_random(begin, end, num_count):
    return list(random.randint(begin, end) for i in range(num_count))
