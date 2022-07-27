def fact(n:int) -> int:
    """Calculate n! iteratively

    Args:
        n (int): _description_
    """
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result


def factorial(n):
    # n! = n* (n-1)!
    """Calculates n! recursively

    Args:
        n (_type_): _description_
    """
    if n <= 1:
        return 1
    else:
        return n* factorial(n-1)


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    if n == 0:
        result = 0
    elif n ==1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(130):
    print(i, fibonacci(i))