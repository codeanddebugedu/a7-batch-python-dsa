"""
ASCII
A -> 65
Z -> 90

a -> 97
z -> 122
"""

# Count the number of alphabets

s = "dhwajk43247DHWAJK^$#*&&(*$    hkjdhwa479)"
count = 0

for ch in s:
    ascii_code = ord(ch)
    if (ascii_code >= 97 and ascii_code <= 122) or (
        ascii_code >= 65 and ascii_code <= 90
    ):
        count += 1

print(count)
