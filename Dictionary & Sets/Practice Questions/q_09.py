# 9. Can you change the values inside a list which is contained in set S
#         S = {8, 7, 12, “Harry”, [1, 2]}

S = {8, 7, 12, "Harry", [1, 2]}

# [1, 2] is the list value in this set
# S.update([1, 2], [3, 4, 5])
# print(S)
# S.remove([1, 2])
# print(S)

# The compiler will throw an error
# S = {8, 7, 12, "Harry", [1, 2]}
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'