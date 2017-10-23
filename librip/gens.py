import random


def field(items, *args):
    if len(args) == 0:
        for i in items:
            yield i
    else:
        if len(args) == 1:
            for item in items:
                if item.get(args[0]) is not None:
                    yield (item.get(args[0]))
        else:
            for item in items:
                result = {arg: item.get(arg) for arg in args if item.get(arg) is not None}
                if len(result) > 0:
                    yield result


def gen_random(begin, end, num_count):
    for _ in range(num_count):
        yield random.randint(begin, end)
