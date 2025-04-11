details = {
    "anirudh": [34, 23, 17, 65, 87],
    "muskan": [36, 85, 71, 45],
    "vandana": [12, 74, 15, 78, 26],
    "sanjay": [34, 47, 11],
    "afsan": [25, 74, 99],
}


print(details.items())
# ans = dict(sorted(details.items(), key=lambda x: x[0]))
# ans = dict(sorted(details.items(), key=lambda x: x[1][-1]))
ans = dict(sorted(details.items(), key=lambda x: sum(x[1])))
print(ans)
