#string and list
p="i am sneha"
q=p.split()
print(q)
l=["a","e","i","o","u"]
for j in q:
    if j[0].lower() in l:
        print(j)

#tuple
t=(78.9,30.9,98,88,89.99)
print(t.count(98))
print(min(t))
print(max(t))
print(sorted(t,reverse=True))

#set

s={"python",9,12}
print(s)
s.add(67)
print(s)
print(s.pop())

#dict
d={"language":"python","rating":7,9:4}
print(d["rating"])
print(d.get("rating"))#if invalid serach it will show none
print(d.get("rat"))
d.update({"rating":0})
print(d["rating"])
d.update({"founder":"guide"})
print(d)
print(d.items())#print in form of tuples
print(d.keys())
print(d.values())
print(d.pop("rating"))
print(d)
print(d.popitem())
print(d)

print("\n")

stu={"name":["sneha","sandra"],"Age":[20,17]}
print(stu)

