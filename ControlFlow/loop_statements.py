for n in range(1, 100):
    for i in range(2, n):
        if n % i == 0:
            # print("{0} is {1} * {2}".format(n, i, n // i))
            break
    else:
        print("{0} is prime number".format(n))
