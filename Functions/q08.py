# 8. Write a python function to print the multiplication table of a given number.


def table(n):
    for i in range(1, 11, 1):
        print(n, "*", i, "=", n*i)


num = int(input("Enter no. for multiplication table: "))
table(num)