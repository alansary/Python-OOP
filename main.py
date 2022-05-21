from decimal import Decimal

myint = 1
mystr = "Mohamed"
mylist = [1, 2, 3, 4, 5]
mybool = True
mynone = None
mytype = type(mylist)


def myfunc():
    pass


print(type(myint))
print(type(mystr))
print(type(mylist))
print(type(mybool))
print(type(mynone))
print(type(mytype))
print(type(myfunc))

print(dir(int)) # Attributes associated with int class

print(Decimal('3.5') + Decimal('3.5'))