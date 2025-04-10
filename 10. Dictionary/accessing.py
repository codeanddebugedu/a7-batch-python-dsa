my_dict = {
    "physics": 98,
    "chemistry": 43,
    "english": 57,
    "hindi": 66,
    "science": 32,
    0: "XYz",
}

# print(my_dict["chemistry"])

print(my_dict.get("chemistry", 0))
