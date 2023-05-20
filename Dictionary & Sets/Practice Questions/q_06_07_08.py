# 6. Create an empty dictionary.
# Allow 4 friends to enter their favorite language as values
# and use keys as their names. Assume that the names are unique.

# 7. If the names of 2 friends are the same; what will happen to the program in Program 6?
# 8. If the languages of two friends are the same; what will happen to the program in Program 6?

# ANSWER TO QUESTION 7: Only one name will be considered as key.
# The value of language will be overridden by the most recent value.

# ANSWER TO QUESTION 8: Different keys may have same values.

Dictionary = {}
name1 = input("Enter name 1: ")
lang1 = input("Enter language 1: ")
name2 = input("Enter name 2: ")
lang2 = input("Enter language 2: ")
name3 = input("Enter name 3: ")
lang3 = input("Enter language 3: ")
name4 = input("Enter name 4: ")
lang4 = input("Enter language 4: ")
tempDictionary = {
    name1: lang1, name2: lang2, name3: lang3, name4: lang4
}
Dictionary.update(tempDictionary)
print(Dictionary)


