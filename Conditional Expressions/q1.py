# 1. Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
if a > b and a > c and a > d:
    greatest = a
elif b > a and b > c and b > d:
    greatest = b
elif c > a and c > b and c > d:
    greatest = c
else:
    greatest = d
print("Largest value is " + str(greatest))