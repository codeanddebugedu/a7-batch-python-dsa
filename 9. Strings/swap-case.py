my_string = "hfejJH&(*$&#@hdkwajhdHdwadDJK3212143WHdwadwaADkjWAB)"

# Swap case
result = ""
for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code >= 65 and ascii_code <= 90:
        new_ascii_code = ascii_code + 32
        result += chr(new_ascii_code)
    elif ascii_code >= 97 and ascii_code <= 122:
        new_ascii_code = ascii_code - 32
        result += chr(new_ascii_code)
    else:
        result += ch
print(result)
