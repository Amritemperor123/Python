import numpy as np
a=[]
b=np.matrix([],[])
c=np.matrix([],[])
for i in range(0,3):
    for j in range(0,3):
        x=int(input(f'Enter element ({i},{j}) of first matrix:'))
        a.append(x)
b=np.matrix(a).reshape(3,3)
print('The system of equation is:\n',b)
a.clear()
for i in range(0,3):
    x=int(input(f'Enter element ({i},0) of second matrix:'))
    a.append(x)
c=np.matrix(a).reshape(3,1)
print('The matrix of coefficient is:\n',c)
print('The solution matrix is:\n',np.linalg.solve(b,c))