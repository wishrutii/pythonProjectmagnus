class Grandparent:
    def a1(self):
        print("2 assets")
class Parent(Grandparent): # a1 and a2 
    def a2(self):
        print("3 assets")
class Son(Parent): # a1,a2 and a3
    def a3(self):
        print("1 asset")
obj1 = Son()
obj1.a1()
obj1.a2()
obj1.a3()
obj2 = Parent()



