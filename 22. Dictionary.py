a={"abc":1,"def":2,"ghi":3}
print('The datatype of the dictionary:',type(a))
print('The dictionary is:',a)
print('The length of the dictionary:',len(a))
print('The item for the key "abc" is:',a["abc"])
del a["abc"]
print('The dictionary sfter deleting the first item:',a)
a["jkl"]=4
print('The dictionary after inserting another item:',a)
print('Calling the keys of the dictionary:',a.keys())
print('Calling the items of the dictionary:',a.items())
print(a.fromkeys("abc"))
a.clear()
print('The cleared dictionary is:',a)