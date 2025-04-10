"""
start=4
end=12

4 5 6 7...11 12
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

for i in range(start, end + 1):
    print(i, end=" ")
