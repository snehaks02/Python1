for i in range(5):
    print(i)


l=[56,"python",8.9]
for i in l:
    print(i)

s={89,"kochi",4.5,89}
if "kochi" in s:
    print("found")
else:
    print("not found")


numbers=list(range(1,51,2))
print(numbers)

number=[n for n in range(1,51) if n%2==0]
print(numbers)


#   print(f"{n} * {num} ={n*num}")


n = int(input("enter number:"))
for i in range (0,n):
    for j in range (0,i+1):
        print("*"," ")

