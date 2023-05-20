# 4. What will be the length of the following set S:
#         S = Set()
#         S.add(20)
#         S.add(20.0)
#         S.add(“20”)

S = set()
S.add(20)
S.add(20.0)  # this 20 is repeated value
S.add("20")
# the length will be 2
print(S)
print(len(S))
