# single inheritance
# class Parent:
#     def fun1(self):
#         print("this is parent class")

# class Child(Parent):
#     def fun2(self):
#         print("this is child class")
# obj = Child()
# obj.fun1()

# multilevel inheritance
# class Parent:
#     def fun1(self):
#          print("this is parent class")
# class Child(Parent):
#     def fun2(self):
#         print("this is child class")
# class Grandchild(Child):
#     def fun3(self):
#         print("this is grandchild class ")
# obj = Grandchild()
# obj.fun1()
# obj.fun2()
# obj.fun3()

# multiple inheritance
# class Mother:
#     def fun1(self):
#          print("this is mother class")
# class Father:
#     def fun2(self):
#         print("this is father class")
# class Child(Mother,Father):
#     def fun3(self):
#         print("this is child class ")
# obj = Child()
# obj.fun1()
# obj.fun2()
# obj.fun3()

# hierarchil inheritance
# class Parent:
#     def fun1(self):
#          print("this is parent class")
# class Child1(Parent):
#     def fun2(self):
#         print("this is child1 class")
# class Child2(Parent):
#     def fun3(self):
#         print("this is child2 class ")
# obj1 = Child1()
# obj2 = Child2()
# obj1.fun1()
# obj2.fun3()


class A:
    def __init__(self):
        print("this is init fun of A")

    def fun1(self):
        print("this is A class")
class B(A):
    def __init__(self):
        print("this is init fun of B")
        super().fun1()
    def fun1(self):
        print("this is A class")

obj = B()
