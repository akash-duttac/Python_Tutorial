# Write a program to format the following letter using escape sequence characters.
#    letter = “Dear Harry, This Python course in nice. Thanks!!”
letter = "Dear Harry, This Python course in nice. Thanks!!"
print("Before: "+letter)
modified_letter = "Dear Harry,\n\tThis Python course in nice.\n\t\tThanks!!"
print("After: " + modified_letter)
