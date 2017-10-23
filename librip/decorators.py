def print_result(func):
    def decorate(*args):
        print(func.__name__)
        result = func(*args)
        if type(result) == list:
            for i in result:
                print(i)
        elif type(result) == dict:
            for key, value in result.items():
                print('{} = {}'.format(key, value))
        else:
            print(result)
        return result

    return decorate
