from typing import Union

def half_double(n: int|float) -> int | float :
    try:
        return n * 2 if n > 10 else n / 2
    except:
        return 0


numbers = [1,2,3,4.5,6,7.8, 10, 15, 20]
half_numbers = [half_double(n) for n in numbers]
print(half_numbers)

