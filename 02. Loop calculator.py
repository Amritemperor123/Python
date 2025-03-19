# this is a simple demostration of how a calculator might work. 
# treat the numerical inputs for specific operations like the buttons you press with symbols in it. 

import math as m

def calculator(a,x):
    if(x >=1 and x <=10):    
        if(x == 1):
            c=m.fabs(a)
            print('The absolute value is:',c)
            x=int(input('Press 11 to exit, 12 to continue.'))
        elif(x == 2):
            c=m.exp(a)
            print('Result of exponential:',c)
            x=int(input('Press 11 to exit, 12 to continue.'))
        elif(x == 3):
            b=int(input('Enter base:'))
            c=m.log(a,b)
            print('Result of logarithm:',c)
            x=int(input('Press 11 to exit, 12 to continue.'))
        elif(x == 4):
            b=int(input('Enter power:'))
            c=m.pow(a,b)
            print('Result after raising to power:',c)
            x=int(input('Press 11 to exit, 12 to continue.'))
        elif(x == 5):
            c=m.sqrt(a)
            print('Square root:',c)
            x=int(input('Press 11 to exit, 12 to continue.'))
        elif(x == 6):
            c=m.sin(a)
            print('Result:',c)
            x=int(input('Press 11 to exit, 12 to continue.'))
        elif(x == 7):
            c=m.cos(a)
            print('Result:',c)
            x=int(input('Press 11 to exit, 12 to continue.'))
        elif(x == 8):
            c=m.tan(a)
            print('Result:',c)
            x=int(input('Press 11 to exit, 12 to continue.'))
        elif(x == 9):
            c=m.degrees(a)
            print('Result:',c)
            x=int(input('Press 11 to exit, 12 to continue.'))
        else:
            c=m.radians(a)
            print('Result:',c)
            x=int(input('Press 11 to exit, 12 to continue.'))
    a=c     
    if(x == 11):
        print('Program aborted.')
    if(x == 12):
        x=int(input('Enter choice:'))
        calculator(a,x)
        
a=int(input('Enter number:'))
print('Enter 1 to calculate absolute value of the given number.')
print('Enter 2 for calculating exponential.')
print('Enter 3 for logarithm.')
print('Enter 4 for raising to power.')
print('Enter 5 for calculating square root.')
print('Enter 6 to calculate sin.')
print('Enter 7 to calculate cos.')
print('Enter 8 to calculate tan.')
print('Enter 9 to converting into radian.')
print('Enter 10 to convert into degrees.')
x=int(input('Enter choice:'))
calculator(a,x)
