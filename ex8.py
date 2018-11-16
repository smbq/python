# 8. Вывести числа от 1 до 100 включительно. Если число делится на 3 то вместо него вывести Foo. Если делится на 5 то вывести Bar. Если делится на 3 и на 5 то вывести FooBar.

for num in range(1, 101):
    if num % 5 == 0:
        if num % 3 == 0:
            print("FooBar")
        else:
            print("Bar")
    elif num % 3 == 0:
        print("Foo")
    else:
        print(num)
