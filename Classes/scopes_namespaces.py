def test_local():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    print(spam)
    do_local()
    print("After local = {0}".format(spam))
    do_nonlocal()
    print("After nonlocal = {0}".format(spam))
    do_global()
    print("After global = {0}".format(spam))


test_local()
print("In global scope", spam)
