class Teacher:
    def english(self):
        print("english language")

class student1(Teacher):
    def math(self):
        print("math subject")
class student2(Teacher):
    pass
obj1 = student1()
obj1.english()
obj2 = student2()
obj2.english()
obj1.math()
