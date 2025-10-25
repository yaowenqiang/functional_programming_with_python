from math import pi
from random import randint
values = [randint(1,5) for _ in range(100)]
areas = {pi * r ** 2 for r in values}
print(areas)
