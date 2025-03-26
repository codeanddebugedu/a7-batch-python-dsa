"""
Ask a start number from user = 8
Ask a end number from user = 18
8 9 10 11...17 18
"""

start_num = int(input("Enter a number = "))
end_num = int(input("Enter a number = "))

i = start_num
while i <= end_num:
    print(i, end=" ")
    i += 1
