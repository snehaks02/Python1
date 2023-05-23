def addition(a,b):
    return a+b
print("sum is:",addition(10,9))

def addition(*num):#take as tuple
    print(num)
addition(10,9,8)

#lambda
x=lambda a,b:a+b
print(x(8,9))
print(type(x))

#facotrial
num=int(input("enter number:"))
fac=1
for i in range (1,num+1):
    fac=fac*i
print(fac)


def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)
print("factorial:",fact(3))
