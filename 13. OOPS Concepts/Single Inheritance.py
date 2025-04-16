# Define a single inheritance named as human and child class a student
# Define a class named Human
class Human:
    def set_human_details(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"


class Student(Human):
    def study(self):
        return f"{self.name} is studying!"


class Employee(Human):
    def work(self):
        return f"{self.name} is working!"


s1 = Student()
s1.set_human_details("Anirudh")
print(s1.speak())
print(s1.study())
