from hw2 import cache


def test_cache():
    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)

    some = 100, 2

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    print(id(val_1))
    print(id(val_2))

    assert val_1 is val_2
