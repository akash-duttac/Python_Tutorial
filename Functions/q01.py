# 1. Write a program using the function to find the greatest of three numbers.
def funcmax(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


num1 = int(input("Enter a: "))
num2 = int(input("Enter b: "))
num3 = int(input("Enter c: "))
print("Maximum =", funcmax(num1, num2, num3))
