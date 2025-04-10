a = [4, 3, 2, 4, 5, 654, 4, 34]
b = a.copy()

print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")

b.append(100)

print(f"a = {a}")
print(f"b = {b}")
