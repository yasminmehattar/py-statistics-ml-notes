# print("Hello, World!")
# print ("Yasmin Mehattar")
# import this

# print ("one")
# print ("two")

# print ("one two")
# print ("one", "two")
# print ("Yasmin Mehattar")
# print ("Yasmin", "Mehattar")

# employee_name = "Yasmin Mehattar"  # str
# employee_grade = 9  # int
# employee_appraisal_grade = 4.5  # float
# employee_married = False  # bool

# print("employee_name:", employee_name)
# print("employee_grade:", employee_grade)
# print("employee_appraisal_grade:", employee_appraisal_grade)
# print("employee_married:", employee_married)

# print("employee_name, employee_grade, employee_appraisal_grade, employee_married")
# print(
#     employee_name,
#     "\t",
#     employee_grade,
#     "\t",
#     employee_appraisal_grade,
#     "\t",
#     employee_married,
# )


# print(
#     type(employee_name),
#     "\t",
#     type(employee_grade),
#     "\t",
#     type(employee_appraisal_grade),
#     "\t",
#     type(employee_married),
# )

# print("=========================")
# print("one")
# print("two")
# print("three")

# print("=========================")
# print("one", end="\n")
# print("two", end="\n")
# print("three", end="\n")

# print("======= Nothing ==================")
# print("one", end="")
# print("two", end="")
# print("three", end="")
# print()

# print("======== Space =================")
# print("one", end=" ")
# print("two", end=" ")
# print("three", end=" ")
# print()

# print("======== Space =================")
# print("one", end="\t")
# print("two", end="\t")
# print("three", end="\t")
# print()

# print("======== Complex Number =================")
# complex_number = 1 + 2j
# print(complex_number)
# print(type(complex_number))
# print(complex_number.real)
# print(complex_number.imag)

# print("======== Convert =================")
# a = "2"
# b = "3"
# print(a + b, type(a + b))

# a_number = int(a)
# b_number = int(b)
# print(a_number + b_number, type(a_number + b_number))

# print(1.1, type(1.1))
# print("1.1", type("1.1"))
# print(1.1, type(1.1))


# print("======== Convert Float =================")
# float_number_1 = 1.2
# float_number_2 = 2.4
# print(float_number_1, float_number_2, end=" ")
# print(float_number_1 + float_number_2, type(float_number_1 + float_number_2))
# print(1.3, int(1.3))
# print(1.4, int(1.4))
# print(1.5, int(1.5))
# print(1.6, int(1.6))
# print(1.7, int(1.7))
# print(1.8, int(1.8))
# print(1.9, int(1.9))
# print(2.0, int(2.0))
# print(1.9, int(3.9999999999999996))

# print("======== Take input from keyboard =================")
# string_1 = input("Press Enter to continue...")
# print(string_1, type(string_1))

# integer_1 = int(input("Press enter an integer: "))
# print(integer_1, type(integer_1))

# integer_1 = float(input("Press enter an decimal number: "))
# print(integer_1, type(integer_1))

# print("======== Reassign assignments =================")

# s = "Yasmin"
# print(s, type(s))

# s = "Mehattar"
# print(s, type(s))

# print("======== Multiple assignments =================")

# a=b=c=1
# print(a, b, c)

# print("========  Print variables   =================")
# a, b, c = 11, 222, 3
# print(a, b, c)
# print("a, b, c", a, b, c)
# print("a {}, b {}, c {}".format( a, b, c))
# print("a %d, b %d, c %d" % ( a, b, c))
#       f-strings (the easiest and most modern way)
# print(f"a {a}, b {b}, c {c}")

# print("========  Comments   =================")
# print ("abc")
# print ("abc")


# num1 = 1
# print ("num1", num1)
# print ("def")

"""
num1 = 1
print ("num1", num1)
print ("def")
"""

"""
num1 = 1
print ("num1", num1)
print ("def")
"""

# str1 = """one
# two
# three
# """
# print(str1)

"""four
five
six
"""

# ==========================

print("========  List   =================")

fruits = ["Apple", 123, "Cherry"]
print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
fruits[1] = "Orange"
print(fruits)
fruits.append("Banana")
fruits.append("Grapes")
print(fruits)
fruits.insert(1, "Banana")
print(fruits)
fruits.remove("Cherry")
print(fruits)
fruits.remove("Banana")
print(fruits)

list1 = [1, 2, 33, 401, 5555, 5555, 6, 7, 8, 9, 10]
print(list1)
list1.remove(401)
print(list1)
list1.pop()
print(list1)
list1.pop(0)
print(list1)

# list1.pop(1)
# print(list1)
# list1.insert(1,3)
# print(list1)

list1[1] = 3
print(list1)

list1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("--------- slice")
print(list1)
print(list1[0:2])
print(list1[3:6])

print("============ count (ele) ==============")
list2 = [11, 22, 33, 33, 44, 55, 33]
print(len(list2))
print(list2.count("33"))
print(list2.count(33))

print("============ tuples ==============")
tuple1 = (11, 2, 3, 4, 3, 5)
print(tuple1, type(tuple1))
print(tuple1[2])
print(len(tuple1))
print(tuple1.count(3))
st2 = sorted(tuple1)
print(st2, type(st2))
st2 = reversed(tuple1)
print(st2, type(st2))

tuple1 = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(tuple1)
print(tuple1[0:2], type(tuple1[0:2]))
print(tuple1[3:6], type(tuple1[3:6]))
print(tuple1)


print("========  String   =================")
my_string = "Hello"
print(my_string, type(my_string))
print(my_string[0])
print(my_string[1])
# my_string[1] = "a"
print(my_string[0:1])
print(my_string[3:60])
