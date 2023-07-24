""" 5. Write a python function to print the first n lines of the following pattern.
***

**       #For n = 3

* """


def func_pattern(n):
    for i in range(n):
        print("*" * (n - i))


n = int(input("Enter n: "))
func_pattern(n)
