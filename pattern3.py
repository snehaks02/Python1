for i in range (1,6):
    for j in range(6-i):
        print(" ",end="")
    print(" * "*i)


for i in range (0,6):
    for j in range(0,i+1):
        print("*",end="")
    print("")
p=1
for i in range (1,6):
    for j in range(6-i):
        print(" ",end="")
    print("*"*p)
    p+=2
