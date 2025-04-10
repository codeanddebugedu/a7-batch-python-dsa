# To create a new list from exisiting list

my_list = [5, 8, 4, 2, 7, 8, 6, 3, 1]

# result = my_list[3:6]
# result = my_list[0:9:-2]
# result = my_list[-5:-2]
# result = my_list[7:2:-1]
# result = my_list[0:]
# result = my_list[:]    # shallow copy, deep copy???
# result = my_list[:4]
# result = my_list[6::-1]
result = my_list[::-1]
print(result)

# result = []
# for i in range(3, 6):
#     result.append(my_list[i])

# print(result)
