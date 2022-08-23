def factorial(n):
    """Calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    print(factorial(900))
except (RecursionError, ZeroDivisionError):
    print("This function cannot calculate factorials that large")

print("Program terminating...")