my_dict = {
    "physics": 98,
    "chemistry": 43,
    "english": 57,
    "hindi": 66,
    "science": 32,
}


print(my_dict)
my_dict["physics"] = 100  # Update (if key exists)
my_dict["pt"] = 43  # Add (if key does not exists)

my_dict.update({"xyz": 1})
print(my_dict)
