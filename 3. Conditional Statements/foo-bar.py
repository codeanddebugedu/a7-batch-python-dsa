"""
num

num divisible by 3 -> FOO
num divisible by 5 -> BAR
num divisible by 3and5 -> FOOBAR
else -> FOOFOOBARBAR
"""

num = int(input("Enter a number = "))
if num % 3 == 0 and num % 5 == 0:
    print("FOOBAR")
elif num % 3 == 0:
    print("FOO")
elif num % 5 == 0:
    print("BAR")
else:
    print("Neither FOO nor BAR")
