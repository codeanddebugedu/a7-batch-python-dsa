"""
{4:7,100:1,5:3......}

Dictionary -> Map/Hash_Map

freq_map
"""

# nums = [4, 5, 4, 4, 4, 3, 2, 3, 2, 1, 2, 2, 100, 2, 3, 4, 4, 4, 5, 4, 4, 3, 2, 4, 4, 2]
nums = "adnwakjdb wahjegudgwahjdgwahdgwahjdwgad     "

# freq_map = {}
# for num in nums:
#     if num in freq_map:
#         # freq_map[num] += 1
#         freq_map[num] = freq_map[num] + 1
#     else:
#         freq_map[num] = 1
# print(freq_map)

freq_map = {}
for num in nums:
    freq_map[num] = freq_map.get(num, 0) + 1
print(freq_map)
