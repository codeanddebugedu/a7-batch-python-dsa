"""
Number of capital letters = 6
Number of small letters = 11
Number of digits = 10
Number of spaces = 7
Number of symbols = 12
"""

my_string = "dwajkl   7329HDAI4367^$73Q&(Y dwdwa   ^&*$(#))"
cap_letters = 0
small_letters = 0
digits = 0
spaces = 0
symbols = 0


for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code >= 65 and ascii_code <= 90:
        cap_letters += 1
    elif ascii_code >= 97 and ascii_code <= 122:
        small_letters += 1
    elif ascii_code == 32:
        spaces += 1
    elif ascii_code >= 48 and ascii_code <= 57:
        digits += 1
    else:
        symbols += 1

print(f"Number of capital letters = {cap_letters}")
print(f"Number of small letters = {small_letters}")
print(f"Number of digits = {digits}")
print(f"Number of spaces = {spaces}")
print(f"Number of symbols = {symbols}")
