def print_result(func):
    def a(arg=None):
        def decorate():
            try:
                result = func(arg)
                print(func.__name__)
                if arg is not None and type(result) is not tuple:
                    result = sorted(filter(lambda x: x is not None, list(i for i in result)),
                                    key=lambda x: x.lower())
                if type(result) == list:
                    print(*result, sep="\n")
                elif type(result) == dict:
                    for key in result.keys():
                        print(key, result.get(key), sep=" = ")
                elif type(result) == tuple:
                    print()
                else:
                    print(result)
                if arg is not None and type(result) is not tuple:
                    return result

            except TypeError:
                print(func())
        return decorate()

    return a
