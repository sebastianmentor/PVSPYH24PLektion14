class A:
    def __init__(self, a):
        self.a = a

    def __eq__(self, value):
        return self.a == value.a

class B:
    ...

var1 = "hej"
var2 = "hej"

print(var1 == var2)

a = A('hej')
b = B()

print(a is b)

a2 = A('hej')

print(a is a2)
print(a == a2)