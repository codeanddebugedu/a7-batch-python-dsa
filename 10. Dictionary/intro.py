# Key-Value (order is maintained)

# Key -> DataType (Immutable) (they can be hashed)
# Value -> DataType (Anything)

my_dict = {
    "physics": 98,
    "chemistry": 43,
    "english": 57,
    "hindi": 66,
    "science": 32,
    1: 100,
    100: 100,
    23.33332: "xyz",
    (1, 2, 3): "Anirudh",
    "marks": [1, 2, 3, 4, 5],
    "physics": 100,
}

print(my_dict)
print(type(my_dict))
