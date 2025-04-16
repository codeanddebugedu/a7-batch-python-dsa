# Make a multiple inheritance example with classes A, B, and C without init methods
# # Define a class named A
class A:
    def __init__(self) -> None:
        print("INIT Method of A class")

    def method_a(self):
        return "Method A from class A"


# # Define a class named B
class B:
    def __init__(self, number) -> None:
        print("INIT Method of B class")
        print(number)

    def method_b(self):
        return "Method B from class B"


# # Define a class named C that inherits from both A and B
class C(A, B):
    def __init__(self) -> None:
        super().__init__()
        A.__init__(self)
        B.__init__(self, 100)
        print("INIT Method of C class")

    def method_c(self):
        return "Method C from class C"


obj = C()
