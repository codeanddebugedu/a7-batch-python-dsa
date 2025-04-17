# Write a program for private access modifier with father and son and make bad habit of father as private


class Father:
    def __init__(self, name, age, bank):
        self.name = name
        self.age = age
        self.__bank = bank

    def get_bank(self):
        return self.__bank


class Son(Father):
    def __init__(self, name, age, bank):
        super().__init__(name, age, bank)


father = Father("John", 50, 1000000)
print(father.name)
print(father.age)
# print(father.__bank)

# Accessing private variable from outside the class without method
print(father._Father__bank)
