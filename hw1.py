import math


def map_every(numbers, func, n):
    assert n >= 0, ValueError
    res = []
    for i in range(0, len(numbers)):
        elem = numbers[i]
        if i % n == 0:
            elem = func(numbers[i])
        res.append(elem)
    return res


# print(map_every([1,2,3,4,5,6], lambda x: x*10, 2))


def sum_by(numbers, func):
    summ = 0
    for num in numbers:
        summ += func(num)

    return summ


def vector_length(x, y, z):

    return math.sqrt(sum_by((x,y,z), lambda x: x**2))


# print(sum_by([1,2,3], lambda x: x*2))
# print(vector_length(1, 2, 2))


def take_while(elements, func):

    res = []

    for elem in elements:
        if not func(elem):
            return res
        res.append(elem)

    return res


# print(take_while([2,4,6,7,8], lambda x: x%2==0))


def count_calls(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} was called {count} times")
        return func(*args, **kwargs)

    return wrapper


# @count_calls
# def greet(name):
#     print(f"hi, {name}!")
#
# greet("Алексей")
# greet("Мария")


def type_check(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal types
            for i in range(len(types)):
                assert isinstance(args[i],types[i]), TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a + b


# print(add(2, 3)) # 5
# print(add(2, '3')) # TypeError: Неверный тип аргумента 2: ожидался <class 'int'>, получен <class 'str'>


def validate_range(min_value, max_value):
    def decorator(func):
        def wrapper(value):
            assert (min_value < value < max_value), ValueError
            return func(value)
        return wrapper
    return decorator


@validate_range(min_value=0, max_value=100)
def set_percentage(value):
    print(f"Установлено значение: {value}%")


# set_percentage(50) # Установлено значение: 50%
# set_percentage(150) # ValueError: Аргумент 'value' имеет значение 150, что выходит за пределы [0, 100]