''' Dictionary is collection of key-value pairs
    -unordered
    -mutable
    -indexed
    -cannot contain duplicate keys '''

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

print(dictionary["Name"])
print(dictionary["Age"])
print(dictionary["dictionaryWithin"])
dictionary["Age"] = 20 # reassign age value
print(dictionary['Roll'])
print(dictionary["dictionaryWithin"]["Languages"])
