# print ("=======for checking python version=========")
# import sys

# print(sys.version)
# print()

# print("==========for checking indentation========")

# if 5 > 2:
#  print("Five is greater than two!") 
# if 5 > 2:
#         print("Five is greater than two!")
# print()
# print("=====we have to use the same number of spaces in the same block of code==========")
# if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!")

'''Python will take it as comment until it is assigned it to a variable'''
"""same as with double quotes too"""
# print()
# print("======vairables=======")
# x=5
# y="yasmin"
# print(x, y, sep=", ")
# print()
# X="Good" #does not overwrite X and x is not same
# print(x,X,y, sep=",")
# a=int("5")
# print(a)
# A=float(6)# by casting we can change the datatype
# print("A")
# print(A)
# print(type(A))
# print(type(a))
# Myvar=45
# print(Myvar)
# d,f,g="orange", "grapes", "apple"
# print(d,f,g)
# d,f,g=["orange", "grapes", "apple"]
# print(d,f,g)
# d=f=g="apple"
# print(d,f,g)
# print(d+f+g)#we can use + operator also to combine for numbers it work as math operator
# h=1
# j=2
# print(h+j)#we can use + operator also to combine for numbers it work as math operator
# print('Hello', 'World')
# import random

# print(random.randrange(1, 10))
# B="yasmin, Mehattar"
# print(B[:5]) #By leaving out the start index, the range will start at the first character
# print(B[4:10])
# print(B[2:])
# print(B.upper())
# print(B.lower())
# print(B.strip())#removes white space from the end or beginning
# print(B.replace("i", "ee"))
# print(B.split(","))
# txt = "Hello \bWorld!"
# print(txt)
# txt= "yasmin \tMehattar"
# print(txt)
# txt="yasmin \\Mehattar"
# print(txt)
# print(f"my name is {txt}")
# print(f"good girl\n{txt}")
# a="Hello"
# b=35
# print(bool(a))
# print(bool(b))
'''Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
 if you have an object that is made from a class with a __len__ function that returns 0 or False:'''
# def myfunction():
#     return True

# if myfunction():
#         print("Yes")
# else:
#         print("NO")
'''List items are ordered, changeable, and allow duplicate values.

List items are indexed,'''
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# list=(("yasmeen", "Mehattar", "sushmit"))
# tuple=("fruits", "names", "greetings")
# print(thislist)
# print(len(thislist))
# print(thislist[3])
# thislist.append("guava")
# print(thislist)
# thislist.insert(2, "watermelon")
# print(thislist)
# thislist.extend(list)
# print(thislist)
# thislist.extend(tuple)
# print(thislist)
# thislist.pop()
# print(thislist)
# thislist.pop(6)
# print(thislist)
# thislist.remove("cherry")
# print(thislist)
# thislist.clear()
# print(thislist)
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)
# thislist.sort()
# print(thislist)#by default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
# thislist.reverse()
# print(thislist)
# mylist=thislist.copy()
# print(mylist)
# mylist_5=list(thislist)
# print(mylist_5)
# mytuple = ("apple", "banana", "cherry")
# print(mytuple)
# my_tuple=(("yasmeen","mehattar"))
# print(my_tuple)
# print(type(my_tuple))
# mylist=list(("list", "tuple"))
# print(type(mylist))
# thistuple = ("apple", "banana", "cherry")
# tuple1=list(thistuple)
# tuple1.append("orange")
# thistuple=tuple(tuple1)
# print(thistuple)
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)#When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
# thistuple=("apple","orange","guava")
# y=list(thistuple)
# y.remove("apple")
# thistuple=tuple(y)
# print(thistuple)
# Newtuple=("apple","orange","guava", "apple","orange","guava")
# (green, yellow, *red)=Newtuple
# print(green)
# print(red)
# thistuple=("orange", "apple",)
# for i in range(len(thistuple)):
#     print(thistuple[i])
# this_tuple=("apple","orange",)
# i=0
# while i<(len(this_tuple)):
#     print(this_tuple[i])
#     i+=1
# mytuple=this_tuple*3
# print(mytuple)  
# new_tuple=(1,2,3) 
# A_tuple=new_tuple+this_tuple
# print(A_tuple)
# x=mytuple.count("orange")#	Returns the number of times a specified value occurs in a tuple
# print(x)
# y=mytuple.index("apple")
# # print(y)
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)
# thisset = {"apple", "banana", "cherry"}

# print("banana" not in thisset)
# list=[1,2,3]
# thisset.update(list)
# print(thisset)
# thisset.add(1)
# print(thisset)
# thisset.remove("banana")
# print(thisset)
# x=thisset.pop()#pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# print(x)
# print(thisset)
set_1={1,2,3,4,4}
set_2={2,1,7,8,9,5}
set_1.add(6)
print(set_1)
# set_1.clear()
# print(set_1)
# set_3=set_1.copy()
# print(set_3)
z=set_1-set_2 # This returns a new set and leaves set1 unchanged.   
print(z)
print(set_1)
set_1-=set_2 #It modifies the original set directly.It does not return anything (technically, it returns None).
print(set_1)
