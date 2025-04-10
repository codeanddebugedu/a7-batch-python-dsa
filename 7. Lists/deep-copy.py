from copy import deepcopy

a = [4, 3, 2, 4, [100, 101, 102], 5, 654, 4, 34]


b = deepcopy(a)

print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")

print(f"id(a[4]) = {id(a[4])}")
print(f"id(b[4]) = {id(b[4])}")


b.append(100)

b[4].append(900)

print(f"a = {a}")
print(f"b = {b}")


a = 10
b = a

b = 100
print(id(a))
print(id(b))
