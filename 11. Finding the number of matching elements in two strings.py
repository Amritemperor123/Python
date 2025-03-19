a=str(input('Enter first string:'))
b=str(input('Enter second string:'))
c=0
for i in range(0, len(a)):
    for j in range(0, len(b)):
        if a[i]==b[j]:
            c=c+1

print('The number of matching characters:',c)