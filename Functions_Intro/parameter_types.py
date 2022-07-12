def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword:.................{}".format(k))
    print("var-keyword:.............{}".format(kwargs))


func(1,2,3,4,5,9, k=6, key1=7, key2=8)




def sum_numbers(*args:float) -> float:
    """Sums numbers

    Returns:
        float: Sum
    """
    result = 0.0
    for n in args:
        result += n
    return result

print(sum_numbers(3,2,4))
print(sum_numbers(3.53,53.5))