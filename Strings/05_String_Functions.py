string = "Hello World!"

# len() returns the length of the string
length = len(string)
print("Length of string = " + str(length))

# endswith()
print(string.endswith("!"))

# count() counts the total no. of occurrences of a character
print(string.count("o"))

# capitalize() capitalizes the first charachter of a given string
cap_str = "laptop"
print(cap_str.capitalize())

# find(word) finds a word and returns the index of first occurrence of word in string
find_str = "Yes no no no no yes"
print(find_str.find("no"))

# replace(old,new) replaces old word with new word
print(find_str.replace("no", "maybe"))