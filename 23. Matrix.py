import numpy as np
def Matrix(n):
    a=[]
    print(type(a))
    b=np.matrix([],[])
    for i in range(0,n):
        for j in range(0,n):
            x=i+j
            a.append(x)
    b=np.matrix(a).reshape(n,n)
    return b

n=int(input("Enter the value of n:"))
y=Matrix(n)
print(y)