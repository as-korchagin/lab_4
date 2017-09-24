# Итератор для удаления дубликатов
class Unique(object):
    ignore_case = False
    items = list()
    result = set()
    index = 0

    def __init__(self, items, **kwargs):
        try:
            self.ignore_case = kwargs['ignore_case']
        except KeyError:
            pass
        self.items = items.copy()

    def __next__(self):
        return_value = None
        if self.index < len(self.items):
            if type(self.items[self.index]) != str:
                if self.items[self.index] not in self.result:
                    self.result.add(self.items[self.index])
                    return_value = self.items[self.index]
            else:
                if not self.ignore_case:
                    if self.items[self.index] not in self.result:
                        self.result.add(self.items[self.index])
                        return_value = self.items[self.index]
                else:
                    if str.lower(self.items[self.index]) not in self.result:
                        self.result.add(str.lower(self.items[self.index]))
                        return_value = self.items[self.index]
            self.index += 1
            return return_value
        else:
            raise StopIteration

    def __iter__(self):
        return self
