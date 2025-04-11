"""
anirudh has scored 432 marks
afsan has scored 231 marks
.
.
.
"""

details = {
    "anirudh": [34, 23, 17, 65, 87],
    "afsan": [25, 74, 99],
    "muskan": [36, 85, 71, 45],
    "vandana": [12, 74, 15, 78, 26],
    "sanjay": [34, 47, 11],
}

# Without any methods
# for name in marks:
#     total = 0
#     n = len(marks[name])
#     for i in range(0, n):
#         total = total + marks[name][i]
#     print(f"{name} has scored {total} marks")

for name, marks in details.items():
    print(name, sum(marks))
