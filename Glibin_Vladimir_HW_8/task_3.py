from functools import wraps


def type_logger(f):
    print(f)

    @wraps(f)
    def wrapper(*args):
        result = [f'{f.__name__}({i}:{type(i)})' for i in args]
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)

print(*a)
