dictionary = {
    "Name": "Akash",
    "Roll": 210523861,
    "Age": 19,
    # nested dictionary
    "dictionaryWithin": {
        "Languages": ["C", "C++"],
        "Room no.s": (1, 3),
    }
}

# keys() -> to print the keys of the dictionary
print(dictionary.keys())
print(list(dictionary.keys()))

# values() -> to print the values of the dictionary
print(dictionary.values())

# items() -> to print the keys & values of the dictionary in (key, value) format
print(dictionary.items())

# prints the entire dictionary
print(dictionary)

newDictionary = {
    "Laptop": "Lenovo",
    "Model": "Ideapad Flex 5"
}

# updates the dictionary from key-value pairs from newDictionary
dictionary.update(newDictionary)
print(dictionary)

# get() -> prints the value associated with the key
# print(newDictionary["Laptop"])
print(newDictionary.get("Laptop"))
print(newDictionary.get("Laptop2"))
# print(newDictionary["Laptop2"]) -> this will throw an error as Laptop2 key does not exist
