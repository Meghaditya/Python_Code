class MyClass:
    i = 345
    s = "hello world"

    def __init__(self):
        self.i = 456
        self.s = "hello friend"

    def f(self):
        return self.s


class Employee:
    pass


e1 = Employee()
e1.name = "john"
e2 = Employee()
e2.age = 30

print(e1.name)
print(e2.age)

c = MyClass()
cf = c.f()
print(c.i)
print(cf)
