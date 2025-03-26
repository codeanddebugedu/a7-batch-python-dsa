"""
1 to 100

3 and 4 divisible -> give the count
"""

i = 1
count = 0
while i <= 100:
    if i % 3 == 0 and i % 4 == 0:
        count += 1
    i += 1

print(count)
