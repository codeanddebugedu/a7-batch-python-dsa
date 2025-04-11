details = [
    {"name": "Anirudh", "physics": 12, "chemistry": 11, "hindi": 98},
    {"name": "Sanjay", "physics": 74, "chemistry": 78, "hindi": 32},
    {"name": "Muskan", "physics": 24, "chemistry": 74, "hindi": 21},
    {"name": "Vandana", "physics": 54, "chemistry": 65, "hindi": 74},
]


# for detail in details:
#     total = detail["physics"] + detail["chemistry"] + detail["hindi"]
#     print(f"{detail['name']} has scored {total} marks")

# details.sort(key=lambda x: x["chemistry"])
# print(details)

x = sorted(details, key=lambda x: x["chemistry"])
print(x)
