# 1. Write definitions for the following two functions using Python
def sumN(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def sumNCube(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i**3
    return sum


n = int(input("Enter a natural number n: "))
print("The sum of the first n natural numbers is:", sumN(n))
print("The sum of the cubes of the first n natural numbers is:", sumNCube(n))
print("------------------------------")

# 2. Write a function to compute the nth Fibonacci number.
def fibonacci(n):
    if n < 0:
        return "Invalid input"
    elif n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


element = int(input("Enter the element number of Fibonacci number: "))
print("The Fibonacci number is:", fibonacci(element))
print("------------------------------")

# 3. Write a function to compute the factorial of a number ‘n’.
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


Number = int(input("Enter the integer number: "))
print("The factorial of the number is:", factorial(Number))
print("------------------------------")
