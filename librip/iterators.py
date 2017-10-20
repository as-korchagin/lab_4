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
        return_value = None
        for i in self.item_gen:
            if type(i) != str:
                if i not in self.result:
                    self.result.add(i)
                    return_value = i
            else:
                if not self.ignore_case:
                    if i not in self.result:
                        self.result.add(i)
                        return_value = i
                else:
                    if str.lower(i) not in self.result:
                        self.result.add(str.lower(i))
                        return_value = i
            return return_value
        else:
            raise StopIteration

    def __iter__(self):
        return self
