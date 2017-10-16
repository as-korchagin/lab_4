import random


def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1 and (item.get(args[0]) is not None):
            yield(item.get(args[0]))
        elif len(args) > 1:
            if None not in set(item.get(arg) for arg in args):
                yield {arg: item.get(arg) for arg in args}


def gen_random(begin, end, num_count):
    for _ in range(num_count):
        yield random.randint(begin, end)
