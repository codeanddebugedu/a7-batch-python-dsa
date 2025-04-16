# Define Multilevel Inheritance with a class named GrandParent, Parent, and Child without __init__ methods
# # Define a class named GrandParent
class GrandParent:
    def grandparent_method(self):
        return "Method from GrandParent"


# # Define a class named Parent that inherits from GrandParent
class Parent(GrandParent):
    def parent_method(self):
        return "Method from Parent"


# # Define a class named Child that inherits from Parent
class Child(Parent):
    def child_method(self):
        return "Method from Child"


# # Create an instance of Child
child = Child()
print(child.child_method())
print(child.parent_method())
print(child.grandparent_method())
