class  computer:
    def Specs(self,r,m):#A FUNCTION RELATED TO OBJECT
        self.RAM=r
        self.model=m
        print(self)

ob=computer() #object creation
ob1=computer()
ob1.Specs("4GB","HP")
ob.Specs("8GB","DELL")
print(ob.RAM)
print(ob.model)
print(ob1.RAM)
print(ob1.model)