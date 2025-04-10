my_string = "hfejJH&(*$&#@hdkwajhdHDJKWHADkjWAB)"

# Remove Space
result = ""

for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code != 32:
        result += ch

print(result)


x = my_string.lower()
print(x)
