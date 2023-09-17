# Calculate factorial
def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)

# User's input


try:
    num = int(input("Input any non-negative integer:"))
    if num < 0:
        print("Factorial is not defined for negative number.")
    else:
        result = factorial(num)
        print(f"lts factorial is {num}{result}")
except ValueError:
    print("Invalid inpuy. Please enter a non-negative integer.")
