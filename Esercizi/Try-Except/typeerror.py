from typing import type_check_only


def printNumber(n):
    if not type(n) is not int:
        raise TypeError("n non è numerico")
    print(n)

print(123)
print('pippo')