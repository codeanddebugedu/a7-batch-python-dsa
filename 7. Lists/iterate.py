# Iterate / Traverse

my_list = [3, 4, 2, 56, 55.67, 44.32, 56, 765, 2, 3432, 43, 645, 765, 876, 876, 867]

n = len(my_list)  # 16

# Iterate by Index
# for i in range(0, n):
#     print(my_list[i])

# for i in range(n - 1, -1, -1):
#     print(my_list[i])

# Iterate by Value
for num in my_list[::-1]:
    print(num, end=" ")
