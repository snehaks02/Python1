
print("palindrome or not")
print("\n")
num=int(input("enter the number"))
rev=0
temp = num
while(num>0):

    dig=num%10
    rev=rev*10+dig
    num=num//10
print("reversed num",rev)

if(rev==temp):
    print("equal")
else:
    print("not")


#another method
a=123
num=str(a)
print(num[::-1])
if(a==num):
    print("true")
else:
    print("false")

#amstrong numb or not
num=int(input("enter the number"))
temp=num
dig=0
while(num>0):
    d=num%10
    dig+=d**len(str(temp))
    num=num//10

if(temp==dig):
    print("amstrong")
else:
    print("not")