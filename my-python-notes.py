# print("Hello, World!")
# print ("Yasmin Mehattar")
# import this

# print ("one")
# print ("two")

# print ("one two")
# print ("one", "two")
# print ("Yasmin Mehattar")
# print ("Yasmin", "Mehattar")

employee_name = "Yasmin Mehattar"  # str
employee_grade = 9  # int
employee_appraisal_grade = 4.5  # float
employee_married = False  # bool

# print("employee_name:", employee_name)
# print("employee_grade:", employee_grade)
# print("employee_appraisal_grade:", employee_appraisal_grade)
# print("employee_married:", employee_married)

print("employee_name, employee_grade, employee_appraisal_grade, employee_married")
print(
    employee_name,
    "\t",
    employee_grade,
    "\t",
    employee_appraisal_grade,
    "\t",
    employee_married,
)


print(
    type(employee_name),
    "\t",
    type(employee_grade),
    "\t",
    type(employee_appraisal_grade),
    "\t",
    type(employee_married),
)

print("=========================")
print("one")
print("two")
print("three")

print("=========================")
print("one", end="\n")
print("two", end="\n")
print("three", end="\n")

print("======= Nothing ==================")
print("one", end="")
print("two", end="")
print("three", end="")
print()

print("======== Space =================")
print("one", end=" ")
print("two", end=" ")
print("three", end=" ")
print()

print("======== Space =================")
print("one", end="\t")
print("two", end="\t")
print("three", end="\t")
print()

print("======== Complex Number =================")
complex_number = 1 + 2j
print(complex_number)
print(type(complex_number))
print(complex_number.real)
print(complex_number.imag)

print("======== Convert =================")
a = "2"
b = "3"
print(a + b, type(a + b))

a_number = int(a)
b_number = int(b)
print(a_number + b_number, type(a_number + b_number))

# print(1.1, type(1.1))
# print("1.1", type("1.1"))
# print(1.1, type(1.1))


print("======== Convert Float =================")
float_number_1 = 1.2
float_number_2 = 2.4
print(float_number_1, float_number_2, end=" ")
print(float_number_1 + float_number_2, type(float_number_1 + float_number_2))
print(1.3, int(1.3))
print(1.4, int(1.4))
print(1.5, int(1.5))
print(1.6, int(1.6))
print(1.7, int(1.7))
print(1.8, int(1.8))
print(1.9, int(1.9))
print(2.0, int(2.0))
print(1.9, int(3.9999999999999996))

print("======== Take input from keyboard =================")
# string_1 = input("Press Enter to continue...")
# print(string_1, type(string_1))

# integer_1 = int(input("Press enter an integer: "))
# print(integer_1, type(integer_1))

integer_1 = float(input("Press enter an decimal number: "))
print(integer_1, type(integer_1))

