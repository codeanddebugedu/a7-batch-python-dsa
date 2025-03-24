name = "Anirudh"
age = 21
gender = "Male"

# Method 1
# print("My name is", name)
# print("My age is", age)
# print("My gender is", gender)
# print("My name is", name, "My age is", age, "My gender is", gender)


# Method 2 (F-Strings)
# print(f"My name is {name}")
# print(f"My age is {age}")
# print(f"My gender is {gender}")
# print(f"My name is {name}, My age is {age} and My gender is {gender}")


# Method 3 (Format specifiers)
# %s -> String, %d -> Integers, %f -> Floats
print("My name is %s" % name)
print("My age is %d" % age)
print("My gender is %s" % gender)
print("My name is %s and age is %d and gender is %s" % (name, age, gender))
