my_string = "hfejJHDEKA43432&(*$&#@hdkwajhdHDJKWHADkjWAB)"

# Uppercase -> Lowercase
result = ""

for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code >= 65 and ascii_code <= 90:
        new_ascii_code = ascii_code + 32
        result += chr(new_ascii_code)
    else:
        result += ch

print(result)
