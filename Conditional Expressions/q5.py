# 5. Write a program that finds out whether a given name is present in a list or not.
nameList = ["Ron", "Roy", "Rob", "Ram"]
check = input("Enter name to check: ")
if check in nameList:
    print("Name is present in the list")
else:
    print("Name not present")