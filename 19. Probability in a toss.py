import random as r
a=[]
n=int(input('Enter number of times a coin is tossed:'))
for i in range(0,n):
    b=r.randint(1,2)
    a.append(b)
h=a.count(1)
t=a.count(2)
print('The probability of head is:',h*100/n)
print('The probability of tail is:',t*100/n)