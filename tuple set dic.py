tuple

a=(1,4,5,6,7,8)
b=(5,6,7,8,9)
print(a)
print(b)
print(type(a))
print(type(b))
c=a+b
print(c)
print(c.index(9))

set

a={0}
b=set()
print(a)
print(type(a))
print(b)
print(type(b))
a={7,8,9,1,2,3,4,5,0}
b={4,5,6,0}
a.update(b)
print(b.issubset(a))
c=a.intersection(b)
print(c)
c.discard(0)
print(c)
print(sum(a))
print(sum(b))

dict

a={}
print(a)
print(type(a))
a={1:["english","science"],2:10.300,3:"bio"}
print(a)
a[3]="siva"
print(a)
print(a.keys())

a=[6,3,5,7,10]
a.sort()
print(a)



