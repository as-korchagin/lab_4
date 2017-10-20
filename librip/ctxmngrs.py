import datetime


class Timer:
    time_in = None

    def __init__(self):
        self.time_in = datetime.datetime.now()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print((datetime.datetime.now() - self.time_in).total_seconds())
        return True
