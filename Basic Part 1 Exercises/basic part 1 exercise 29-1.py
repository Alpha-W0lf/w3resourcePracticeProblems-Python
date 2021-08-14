# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in
# color_list_2. Go to the editor
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

# answer = set([])
#
# def compare(x, y):
#     for i in x:
#         if i in y:
#             continue
#         else:
#             answer.add(i)
#     print(answer)
#
#
# compare(color_list_1, color_list_2)

final = color_list_1 - color_list_2

print(final)