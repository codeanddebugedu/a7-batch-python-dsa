class Student:
    """This creates a student object with name, age, and roll_no"""

    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}"

    def __repr__(self) -> str:
        return f"Student(name={self.name}, age={self.age}, roll_no={self.roll_no})"

    def __len__(self) -> int:
        return len(self.name)

    def __add__(self, obj):
        return self.age + obj.age

    def __mul__(self, obj):
        return self.age * obj.age

    def __sub__(self, obj):
        return self.age - obj.age

    def __truediv__(self, obj):
        return self.age / obj.age

    def __floordiv__(self, obj):
        return self.age // obj.age

    def __mod__(self, obj):
        return self.age % obj.age

    def __pow__(self, obj):
        return self.age**obj.age

    def __eq__(self, obj):
        return self.age == obj.age


student1 = Student("John", 20, 1)
student2 = Student("Jane", 20, 2)

print(student1 + student2)
print(student1 == student2)

# Difference between __str__ and __repr__
# __str__ is used to return a string representation of the object
# __repr__ is used to return a string representation of the object that is more detailed

print(student1)
print(repr(student1))
