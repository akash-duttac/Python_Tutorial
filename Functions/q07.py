# 7. Write a python function to remove a given word from a list and strip it at the same time.


def removal(s, w):
    newStr = s.replace(w, "").strip()
    return newStr


string = str(input("Enter the string: "))
word = str(input("Enter the word: "))
finalstr = removal(string, word)
print(finalstr)