def Push(a,b):
    a.append(b)
def push(a,x):
    if(x==1):
        b=int(input('Enter item to push:'))
        Push(a,b)
        print('The new queue is:',a)
        x=int(input('Enter 1 to push, 2 to pop, 3 to exit:'))
        if(x==1):
            push(a,x)
        elif(x==2):
            pop(a,x)
        else:
            print('Program aborted!')
def pop(a,x):
    if(x==2):
        if(len(a)<=0):
            print('\n\tCannot perform pop!\n\tThe queue is empty!\n')
        else:
            print('The popped element is:',a[0])
            a.pop(0)
            print('The popped queue is:',a)
        x=int(input('Enter 1 to push, 2 to pop, 3 to exit:'))
        if(x==1):
            push(a,x)
        elif(x==2):
            pop(a,x)
        else:
            print('Program aborted!')
a=[]
n=int(input('Enter initial size of the queue:'))
for i in range(0,n):
    b=int(input(f'Enter element {i+1} of queue:'))
    Push(a,b)
x=int(input('Enter 1 to push, 2 to pop:'))
if(x==1):
    push(a,x)
elif(x==2):
    pop(a,x)
else:
    print('Program aborted!')