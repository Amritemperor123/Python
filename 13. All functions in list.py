a=[]
n=int(input("Enter size of list: "))
for i in range(n):
    b=int(input("Enter input #{i + 1}: "))
    a.append(b)
print("The list is:",a)
print('The copied list is:',a.copy())
x=int(input('Enter element to get value:'))
print('The index of the element is:',a.index(x))
x=int(input('Enter index to insert new item:'))
y=int(input('Enter input:'))
a.insert(x,y)
print('The new list is:',a)
x=int(input('Enter element to remove:'))
a.remove(x)
print('The new list is:',a)
x=int(input('Enter index to remove:'))
a.pop(x)
print('The new list is:',a)
a.reverse()
print('The reversed list is:',a)
a.sort()
print('The sorted list is:',a)
a.clear()
print('The cleared list is:',a)