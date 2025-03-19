x=str(input('Enter string:'))
print('Capitalized string:',x.capitalize())
print('Titled string:',x.title())
print('Uppercased string:',x.upper())
print('Lowercased string:',x.lower())
print('Swapcased string:',x.swapcase())
if(x.islower()==True):
    print('All alphabets in the string is in lowercase.')
else:
    print('Not all alphabet in the string is in lowercase.')
if(x.isupper()==True):
    print('All alphabets is the string is in uppercase.')
else:
    print('Not all alphabet in the string is in uppercase.')
if(x.istitle()==True):
    print('The string is in titlecase.')
else:
    print('The string is not in titlecase.')
print('Stripped string:',x.strip())
print('Stripped string from beginning:',x.lstrip())
print('Stripped string from end:',x.rstrip())
y=str(input('Enter delimiter:'))
print('String after splitting:',x.split(y))
print('String after partitioning:',x.partition(y))
y=str(input('Enter string to find:'))
if(x.find(y)==-1):
    print('String not present.')
else:
    print('String has first index:',x.find(y))
    print('String has last index:',x.rfind(y))
y=str(input('Enter string to count:'))
print('The string has occured:',x.count(y),' times')
if(x.isspace()==True):
    print('The string consists of whitespace.')
else:
    print('This string has some elements except whitespaces.')
if(x.isalpha()==True):
    print('All elements of this string are alphabets.')
else:
    print('Not all elements of this string is alphabet.')
if(x.isalnum()==True):
    print('This string consists of only alphabets and numbers.')
else:
    print('This string does not consists of only alphabets and numbers.')
y=str(input('Enter string to verify:'))
if(x.startswith(y)==True):
    print('The string starts with this given input.')
else:
    print('The string dose not starts with this given input.')
if(x.endswith(y)==True):
    print('The string ends with this given input.')
else:
    print('The string dose not ends with this given input.')