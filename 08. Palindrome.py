# what is a plindrome you might ask?
# it's a number which reads same both ways, like 12311 or 565

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
