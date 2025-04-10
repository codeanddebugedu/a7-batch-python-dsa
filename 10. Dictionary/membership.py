# in / not in (boolean)


nums = [4, 5, 4, 4, 4, 3, 2, 3, 2, 1, 2, 2, 1, 2, 3, 4, 4, 4, 5, 4, 4, 3]  # O(n)
my_dict = {
    "physics": 98,
    "chemistry": 43,
    "english": 57,
    "hindi": 66,
    "science": 32,
    0: "XYz",
}


n = "dwadwa"
if n in my_dict:
    print("Yes")
else:
    print("No")
