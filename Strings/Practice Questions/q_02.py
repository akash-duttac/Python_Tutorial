# Write a program to fill in a letter template given below with name and date.
#    letter = ‘’’ Dear <|NAME|>,
#                         You are selected!
#                         <|DATE|>

letter = '''Dear name,
                    You are selected!
                    date'''
name = input("Enter name: ")
date = input("Enter date: ")
letter = letter.replace("name", name)
letter = letter.replace("date", date)
print(letter)