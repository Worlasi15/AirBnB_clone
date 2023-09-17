# Calculate factorial
def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)


try:
    num = int(input("Input any non-negative integer:"))
    if num < 0:
        print("Factorial is not defined for negative number.")
    else:
        result = factorial(num)
        print(f"Its factorial is {result}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
