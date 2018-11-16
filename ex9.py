#9. Hard mode, optional: Реализовать фабрику декораторов, инициализируемую с натуральным числом n, производящую умножение результата декорируемой функции на n если операция применима, иначе возвращающих None.

def dec(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs) * n
            except TypeError:
                return None
        return wrapper
    return inner


@dec(10)
def add(x, y, z):
    return x + y + z


@dec(5)
def spam(n):
    return ['SPAM', '!' * n]


@dec(3)
def ls():
    return {1, 2, 3, 4}


print(add(5, 5, 5))
print(spam(3))
print(ls())
