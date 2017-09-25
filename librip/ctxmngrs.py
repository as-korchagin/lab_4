import datetime


# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5

class Timer:
    time_in = None

    def __init__(self):
        self.time_in = datetime.datetime.now()

    def __enter__(self):
        return self.time_in

    def __exit__(self, *args):
        print((datetime.datetime.now() - self.time_in).total_seconds())
        return True
