# Lambda = Anonymous (they dont have a name)
# Your function contains one liners


# def odd_even(num: int) -> bool:
#     return num % 2 == 0


total_marks = lambda phy, chem, eng: phy + chem + eng
func = lambda num: num % 2 == 0

# print(func(10))
# print(func(11))

print(total_marks(10, 20, 30))
