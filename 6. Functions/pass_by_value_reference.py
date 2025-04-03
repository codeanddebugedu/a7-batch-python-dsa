"""
Pass by Value (Immutable)
int,str,float,tuple

Pass by Reference (Mutable)
list,set,dictionary
"""


def change(a, b):
    print(f"Address of a inside = {id(a)}")
    b = 1000
    a.append(100)
    print(f"Address of a inside = {id(a)}")


a = [1, 2, 3, 4, 5]
print(f"Address of a outside = {id(a)}")
b = 100

change(a, b)
print(a)
print(b)
