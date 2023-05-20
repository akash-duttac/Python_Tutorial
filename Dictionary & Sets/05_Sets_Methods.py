tempSet = set()
# add() -> to add values to the set
tempSet.add(1)
tempSet.add(2)
tempSet.add(3)
tempSet.add(4)
tempSet.add(5)
tempSet.add(6)
print(tempSet)

# len(<set_name>) -> returns the length of the set
print(len(tempSet))

# remove() -> deletes element from set
tempSet.remove(3)
print(tempSet)

# pop() -> returns an element removed from set
print(tempSet.pop())

# clear() -> empties the set
tempSet.clear()
print(tempSet)

set1 = {1, 3, 5, 7, 0, 99}
set2 = {2, 4, 6, 8, 0, 99}

# union()
setUnion = set1.union(set2)
print(setUnion)

# intersection()
setIntersection = set1.intersection(set2)
print(setIntersection)

