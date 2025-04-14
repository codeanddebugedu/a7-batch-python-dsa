class Student:
    # Class Variables / Attributes

    # Magic Methods
    def __init__(self, roll_no, name, gender, age) -> None:
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.age = age

    # Methods (functions)
    def display(self):
        print(f"Roll number = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")

    # def get_details(self, roll_no, name, gender, age, school="XYZ"):
    #     self.roll_no = roll_no
    #     self.name = name
    #     self.gender = gender
    #     self.age = age
    #     self.school = school

    # def get_details(self):
    #     self.roll_no = int(input("Enter roll no = "))
    #     self.name = input("Enter name = ")
    #     self.gender = input("Enter gender = ")
    #     self.age = int(input("Enter age = "))


s1 = Student(1, "ANirudh", "Male", 11)
s1.display()
