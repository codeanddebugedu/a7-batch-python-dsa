"""
Keep asking characters from a user

q, dont stop
"""

my_string = ""

while True:
    ch = input("Enter a character = ")
    if ch == "q" or ch == "Q":
        break
    my_string += ch

print(my_string)
