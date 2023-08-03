# oops stands for Object oriented Programming. This is a part of functional Programming or standalone programming.
# class is a blueprint of an application. variables and functions are properties of class,
class Sample:
    a=10
    b=20
    def m1(self):
        print("m1 fucntion")

obj1 = Sample() # we can use anything instead of obj1. creating an object for class. object allocates a memory for
# the class properties
print(obj1.a)
obj1.m1()# calling the m1 function name to get results.
print(obj1.a - obj1.b)
