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
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
list=(("yasmeen", "Mehattar", "sushmit"))
tuple=("fruits", "names", "greetings")
print(thislist)
print(len(thislist))
print(thislist[3])
thislist.append("guava")
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)
thislist.extend(list)
print(thislist)
thislist.extend(tuple)
print(thislist)
thislist.pop()
print(thislist)
thislist.pop(6)
print(thislist)
thislist.remove("cherry")
print(thislist)
thislist.clear()
print(thislist)