a=2
b=3
c=-1
d=-0.5
m=-b//a-(-1)*c*b/d**c%c%d+(0 and 1 or not 0)

print(m)

a = 10
b = 20
c = (a if a>b else b)*2
d = list(range(10))
d[0] = c
print(d[0:6:2])

def foo(x):
    x += 1
    if x<20:
        return foo(x)+1
    else:
        return x

x = 10
print(foo(x))

def change1(mylist):
    mylist[0] = 2
    print(mylist)
    return

def change2(mylist):
    mylist = [1,2,3,4]
    print(mylist)
    return

mylist = [10,20,30]
change1(mylist)
print(mylist)
change2(mylist)
print(mylist)


import numpy as np
x1 = np.arange(8)
x2 = np.reshape(x1,(2,4))
print(np.roll(x2,1,axis=0))