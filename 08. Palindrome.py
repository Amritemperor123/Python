x=int(input('Enter any number:'))
a=x
b=0
while (a!=0):
    y=int(a%10)
    b=b*10+y
    a=int(a/10)
if x==b:
    print(x,' is a palindrome.')
else:
    print(x,' is not a palindrome.')