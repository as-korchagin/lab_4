# Итератор для удаления дубликатов
class Unique(object):
    ignore_case = False
    items = list()
    result = set()
    index = 0

    item_gen = None

    def __init__(self, items, **kwargs):
        try:
            self.ignore_case = kwargs['ignore_case']
        except KeyError:
            pass
        self.item_gen = items

    def __next__(self):
        for i in self.item_gen:
            if type(i) != str:
                if i not in self.result:
                    self.result.add(i)
                    return i
            if self.ignore_case:
                if i in self.result:
                    continue
                else:
                    self.result.add(i)
                    return i
            else:
                if i.lower() in self.result:
                    continue
                else:
                    self.result.add(i.lower())
                    return i
        else:
            raise StopIteration

    def __iter__(self):
        return self
