for i in range(1, 6):
    for j in range(1, 5 - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(1, 5 - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()
