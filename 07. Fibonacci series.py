def fibo(n):
    x=0
    y=1
    z=y
    count=x
    while count<n:
        print(y,end=" ")
        count=count+1
        x, y=y, z
        z = x + y
    print()
        
n=int(input('Enter the number of elements of the series:'))
print("The Fibonacci series is:")
fibo(n)