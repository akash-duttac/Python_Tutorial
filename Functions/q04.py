# 4. Write a recursive function to calculate the sum of first n natural numbers.
def sum_natural_recursive(n):
    if n == 0:
        return 0
    return n + sum_natural_recursive(n-1)


print("Sum up to n natural no.s")
num = int(input("Enter n: "))
ans = sum_natural_recursive(num)
print("Sum =", ans)
