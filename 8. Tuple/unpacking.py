# a, b, c, d = (5, 7, 4, 1)
# a, b, c, d = [5, 7, 4, 1]
# a, b, c, d = "guhr"

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))

# a, b = 10, 20
# print(a)
# print(b)

from typing import Tuple


# It returns both total,percentage scored
def calculate(phy: int, chem: int, eng: int, hindi: int) -> Tuple[int, float]:
    total = phy + chem + eng + hindi
    percentage = total / 400 * 100
    return total, percentage


t, p = calculate(43, 65, 32, 21)
print(t)
print(p)
