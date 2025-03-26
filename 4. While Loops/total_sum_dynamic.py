"""
Ask a start number from user = 1
Ask a end number from user = 984

8 + 9 +10+11+....17+18
"""

start_num = int(input("Enter a number = "))
end_num = int(input("Enter a number = "))
total = 0
i = start_num

while i <= end_num:
    total = total + i
    i += 1

print(total)
