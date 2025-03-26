"""
Start = 19
End = 10
19 18 17...11 10
"""

start_num = int(input("Enter a number = "))  # 19
end_num = int(input("Enter a number = "))  # 11

i = start_num
while i >= end_num:
    print(i, end=" ")
    i -= 1
