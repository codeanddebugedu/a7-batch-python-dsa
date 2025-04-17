# Access Modifiers (Encapsulation also known as data hiding):
# 1. Public
# 2. Protected
# 3. Private


# # Write a program for public access modifier
# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary


# emp = Employee("John", 30, 50000)
# print(emp.name)
# print(emp.age)
# print(emp.salary)


# Write a program for protected access modifier and make salary as protected
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self._salary = salary

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    def _login(self):
        print("Login successful")


emp = Employee("John", 30, 50000)
print(emp.name)
print(emp.age)
print(emp.get_salary())
emp.set_salary(60000)
print(emp.get_salary())
