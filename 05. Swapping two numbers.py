def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print('Swapped numbers are: a=',a,' b=',b)

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
swap(a,b)