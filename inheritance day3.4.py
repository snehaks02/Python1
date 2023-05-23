#multiple inheritance
class A:
    def __init__(self):
        C.__init__(self)
        self.a=10
        self.b=30




class C:
    def __init__(self):
        self.c=11
        self.d=12

class D(A,C):
    def sub(self):
        print(self.a-self.c)
ob1=D()
ob1.sub()

#multilevel
class B(A):
    def add(self):
        print(self.a+self.b)

class E(B):
    def mul(self):
        print(self.a*self.b)

ob2=E()
ob2.mul()

#