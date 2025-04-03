def change():
    global a, b
    print("Inside function 👇")
    print(f"id(a) -> {id(a)}, id(b) -> {id(b)}")
    a = 100
    b = 105
    # print(a)
    # print(b)


a = 5
b = 15
print("Outside function 👇")
print(f"id(a) -> {id(a)}, id(b) -> {id(b)}")
change()
# print("-------")
print(a)
print(b)
