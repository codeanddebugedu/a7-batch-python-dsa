"""
Case 1
Enter start number = 5
Enter end number = 12
5 6 7 8...11 12


Case 2
Enter start number = 15
Enter end number = 8
8 9 10 11..14 15
"""

start_num = int(input("Enter a number = "))
end_num = int(input("Enter a number = "))

if start_num < end_num:
    s = start_num
    e = end_num
else:
    s = end_num
    e = start_num

while s <= e:
    print(s, end=" ")
    s += 1
