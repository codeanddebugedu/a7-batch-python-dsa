my_dict = {
    "physics": 98,
    "chemistry": 43,
    "english": 57,
    "hindi": 66,
    "science": 32,
}

# By Keys (100% question can be solved)
# for k in my_dict:
#     print(k, my_dict[k])

# By Keys
# for k in my_dict.keys():
#     print(k, my_dict[k])

# for v in my_dict.values():
#     print(v)

# for k, v in my_dict.items():
#     print(k, v)

total = 0
for k in my_dict:
    total = total + my_dict[k]

print(total)
