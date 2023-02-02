def class_log(some_arg):
    def decorator(some_class):
        def decorator_for_func(func):
            def wrapper(*args, **kwargs):
                if some_class.__getattribute__(some_class, func.__name__):
                    some_arg.append(func.__name__)
                return func(*args, **kwargs)

            return wrapper

        for function in some_class.__dict__.values():
            if callable(function):
                setattr(some_class, function.__name__, decorator_for_func(function))
        return some_class

    return decorator


vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2)
v[0] = 2
print(
    vector_log
)
