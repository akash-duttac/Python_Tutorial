# 2. Write a python program using the function to convert Celsius to Fahrenheit.
# f = 1.8c + 32
def func_convertor(cel):
    return 1.8*cel + 32


temp = float(input("Enter temperature in Celsius?: "))
print("Temperature in Fahrenheit is", func_convertor(temp))