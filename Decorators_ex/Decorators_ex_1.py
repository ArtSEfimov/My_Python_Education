def under_decor(param='world'):
    def make_decor(func_decor):
        def wrapper(real_func):
            def inner(*args, **kwargs):
                return func_decor(real_func, param, *args, **kwargs)

            return inner

        return wrapper

    return make_decor


@under_decor('xyz')
def decor(f, param, *args, **kwargs):
    print('hello', param)
    return f(*args, **kwargs)


@decor
def func(a, b):
    return a + b


print(
    func(1, 2)
)
