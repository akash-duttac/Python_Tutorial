# 1. Write a program to create a dictionary of Hindi words with values as their English translation.
#     Provide the user with an option to look it up!
HindiToEnglish = {
    "billi": "cat",
    "kutta": "dog",
    "baarish": "rain"
}
string = input("Enter word to search for?: ")
print(HindiToEnglish.get(string))