# Hybrid Inheritance Example (very simple, no __init__)


class A:
    def method_a(self):
        return "A"


class B(A):  # Single inheritance from A
    def method_b(self):
        return "B"


class C(A):  # Single inheritance from A
    def method_c(self):
        return "C"


class D(B, C):  # Multiple inheritance from B and C
    def method_d(self):
        return "D"


# Create object of D
obj = D()
print(obj.method_a())  # From A
print(obj.method_b())  # From B
print(obj.method_c())  # From C
print(obj.method_d())  # From D
print(D.mro())
