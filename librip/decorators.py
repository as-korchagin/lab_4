def print_result(func):
    def decorate():
        result = func()
        print(func.__name__)
        if type(result) == list:
            print(*result, sep="\n")
        elif type(result) == dict:
            for key in result.keys():
                print(key, result.get(key), sep=" = ")
        else:
            print(result)

    return decorate
