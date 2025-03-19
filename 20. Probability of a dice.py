import random as r
a=[]
n=int(input('Enter number of times a dice is thrown:'))
for i in range(0,n):
    b=r.randint(1,6)
    a.append(b)
for i in range(1,7):
    o=a.count(i)
    print(f'The probability of {i} is:',o*100/n,'%')