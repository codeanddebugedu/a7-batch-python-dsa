# Define a single inheritance named as human and child class a student
# Define a class named Human
class Human:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"


class Student(Human):
    def __init__(self, n):
        super().__init__(n)
        print("INIT Method of Student class")

    def study(self):
        return f"{self.name} is studying!"


s1 = Student("Anirudh")
print(s1.study())
