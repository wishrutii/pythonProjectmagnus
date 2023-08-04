class Sample:
    def m1(self):
        print("welcome m1 function")
class Demo(Sample): # another class in inheriting the previous class(sample), so that way we don't have to create so
    #  many objects.
     def m2(self):
         print("welcome m2 function")
obj1 = Demo() # we don't need to create another object for class sample bc demo inherited it.
obj1.m1()
obj1.m2()
