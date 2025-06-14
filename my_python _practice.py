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
# set_1={1,2,3,4,4}
# set_2={2,1,7,8,9,5}
# set_1.add(6)
# print(set_1)
# # set_1.clear()
# # print(set_1)
# # set_3=set_1.copy()
# # print(set_3)
# z=set_1-set_2 # This returns a new set and leaves set1 unchanged.   
# print(z)
# print(set_1)
# set_1-=set_2 #It modifies the original set directly.It does not return anything (technically, it returns None).
# print(set_1)
# set_1.discard(4)
# print(set_1)
# G=set_1&set_2# The set to search for equal items in
# print(G)
'''Return True if all items in set x are present in set y: issubset() Use <= as a shortcut
   Return True if no items in set x is present in set y:isdisjoint()
   Return True if all items set y are present in set x: issuperset()Use >= as a shortcut
   The pop() method removes a random item from the set.
   symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
   As a shortcut, you can use the ^ operator instead
'''
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# y=thisdict.get("year")
# print(x , y)
# Z=thisdict.keys()
# print(Z)
# thisdict['color']="white"
# print(Z)
# t=thisdict.values()
# print(t)
# thisdict["model"]="mast"
# print(t)
# r=thisdict.items()
# print(
# )
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# thisdict.pop("model")
# print(thisdict)
# thisdict.popitem()
# print(thisdict)
# del thisdict["brand"]
# print(thisdict)
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#     print(x)#for printing keys
# for x in thisdict:
#     print(thisdict[x])#for printing the values

# for x in thisdict.values():
#     print(x)
# for x,y in thisdict.items():
#     print(x,y)
# mydict=thisdict.copy()
# print(mydict)
# my_dict=dict(thisdict)
# print(my_dict)
# child1={
#     "name":"yasmin",
#     "year": 2020
# }
# child2={
#     "name":"mehattar",
#     "year": 2021
# }
# child3={
#     "name":"YMehattar",
#     "class": "ten",
#     "year":2022
# }
# myfamily= {
#     "one":child1,
#     "two":child2,
#     "three":child3
# }
# print(myfamily)
# print(myfamily["three"])
# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")
# a = 200
# b = 33
# c = 500
# if b<a or c<b:
#     print("one condition is true")
    
# day = 8
# match day:
#     case 1|2|3|4|5:
#         print("this is a weekday")
#     case 6|7:
#         print("this is a weekend")
#     case _:
#         print("no other day")

# day = 6
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday") 
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("THursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("sunday")
#     case _:
#         print("no other day")   
# month = 7
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5 if month in(1,2,3,4):
#     print("A weekday in Jan-April")
#   case 1 | 2 | 3 | 4 | 5 if month == 5:
#     print("A weekday in May")
#   case _:
#     print("No match")    

# i=1
# while i < 6:
#     print(i)
#     i += 1

# i=1
# while i < 9:
#     print(i)
#     if i == 6:
#         break
#     i +=1
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         i += 1  # increment before continue
#         continue
#     i += 1

# i=1
# while i < 6:
#       i += 1
#       if i == 3:
#           continue
#       print(i)
# fruits = ["banana","apple","guava"]
# for x in fruits:
#      print(x)
# fruits = ["banana","apple","guava"]
# for x in fruits:
#      print(x)
#      if x == "apple":
#            break
# fruits = ["banana","apple","guava"]
# for x in fruits:
#      if x == "apple":
#           break
#      print(x)
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x) 
#   for x in range(6):
#    print(x) 
# for x in range(2, 6):
#   print(x)
# for x in range(2,100,5):
#    print(x)
# else:
#    print("All finished")
# for x in range(2,50):
#    if x == 25:
#       continue
#    print(x)
# else:
#    print("All finished")
# for x in range(2,50):
#    if x == 25:
#       break
#    print(x)
# else:
#    print("All finished")
# for x in range(2,50):
#     print(x)
#     if x == 25:
#       continue
  
# else:
#    print("All finished")
# for x in range(2, 30):
#     print(x)  # This always runs
#     if x == 25:
#         continue  # Skips the rest below for x == 25
#     print(f"{x} is not 25")  # This will NOT run when x == 25
# else:
#     print("All finished")
# for x in range(2, 30):
#     print(x)  # This always runs
#     if x == 25:
#         break  # stops the loop immediately if x == 25
#     print(f"{x} is not 25")  # This will NOT run when x == 25
# else:
#     print("All finished")
# -----Nested loops -------
# fruits =["apple","banana","guava"]
# biscuits =["cookies","goodday","mariegold"]
# for x in fruits:
#     for y in biscuits:
#         print(x, y)

# for x in [0, 1, 2]:
#   pass

#------Functions------------
# def fruits():
#     print("fruits is function name")
# fruits()

# def fruits(one,two):
#     print(one+" "+ two +" "+ 'are fruits')
# fruits("apple", "banana")
# fruits("guava","vana")

# def fruits(*names):
#     print("i have fruits those are:" + " ," .join(names))
# fruits(" apple", "guava","banana")

# def fruits(*names):
#     print("My favaourite fruit is:" + " "+ names[3])
# fruits("apple", "banana" , "guava","berry") 
 
# def fruits(three, one, two):
#     print("my favourite fruit is:"+ " "+ two)
# fruits(one="apple",two="banana", three="guava")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def function(food):
#     for x in food:
#         print(x)

# fruits=["apple","banana","guava"] 
# gadgets=["tv","computer","mouse"]

# function(fruits)
# function(gadgets)  

# def yasmin():
#     names=["yaseen","gouse","shakerun"]
#     for x in names:
#         print(x)
# yasmin()

# def mehattar(x):
#     return 3*x
# print(mehattar(3))
# print(mehattar(6))
# print(mehattar(9))
# print(mehattar(12))

# def my_function(x, /):
#   print(x)

# my_function(3)

# def my_function(x):
#   print(x)

# my_function(x = 3)

# def my_function(*, x):
#   print(x)

# my_function(x = 3)

# x=lambda a:a+6
# print(x(6))

# x=lambda a,b:a*b
# print(x(6,6))

# def myfun(n):
#     return lambda a:a*n
# mytwo=myfun(2)
# mythree=myfun(3)
# print(mytwo(6))
# print(mythree(6))

# cars=["apple","banana","apple","guava"]
# cars.remove("apple")
# cars.pop(2)
# print(cars)

# class one:
#     X=6
# print(one)
# y=one()
# print(y.X)

class myclass:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(a):
        return f"{a.name} ({a.age})"
p= myclass( 'John',30)
print(p)

class yasmin:
    def __init__(yes, name, age):
        yes.name=name
        yes.age=age
    def mehattar(no):
        print("my name is"+ " "+no.name +" " +"my age is"+ str(no.age))
obj=yasmin("good",25)
obj.mehattar()


    


