def fib(n):
    a, b = 0, 1
    while b < n:
        print(a, " ")
        a, b = b, a + b


# arbitrary argument lists
def write_multiple_items(*args, sep="/"):
    return sep.join(args)


print(write_multiple_items("1", "2", "3", sep="."))


# lambda function
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(3))
