x=int(input('Enter the range for prime numbers:'))
for i in range(2,x):
    k=0
    a=i+1
    y=int(pow(a,1/2))
    for j in range(2,y+1):
        if(a%j != 0):
            k=k+1
    if(k == 0):
        print(i,'is a prime number.')