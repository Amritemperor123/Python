def fact(a):
    b=1
    for x in range (1,a+1):
        b=b*x
        x=x+1
    print('The factorial of number ',a,' is: ',b)

a=int(input('Enter number:'))
fact(a)