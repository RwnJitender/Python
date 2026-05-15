# num = 34
# print(num)

# num = 45

# del num

# print(num)


# Data types -> Primitive  || Collection


# Primitive - > int float bool string complex
# Collection - > string list tuple set dict

# num = 23
# point = 34.4
# name = "rahul"
# name2='sumit'
# choice = True
# choice2 = False
# com = 3+4j

# type()

# print(type(num))
# print(type(point))
# print(type(name))
# print(type(name2))
# print(type(choice))
# print(type(choice2))
# print(type(com))


# num = input("Enter a num : ");
# num2 = input("Enter a num : ");

# print(type(num))
# print(type(num2))

# print("The value of sum is ", num+num2)

# Type Converstion -> Implicit Explicit

# num = 34.4
# num2 =" 45"

# print(num+num2)

# Type casting consutructors

# int() str() float() bool()

# num = 23

# print(float(num))
# print(str(num))
# print(bool(num))

# print(int(23))
# print(int(23.99))
# print(int(True))
# print(int(False))
# print(int("sgsh"))

# print(float(34))
# print(float(True))
# print(float(False))

# Truthy Falsy(0,"",False) Values

# print(bool(23))
# print(bool(23.4))
# print(bool("ksdf"))
# print(bool(""))
# print(bool(0))
# print(bool(-1))

# a = int(input("Enter a num :"))
# b = input("Enter a num :")

# print(a+int(b))

# id()  memory address

# num = 34

# print(id(num))

name = input("Enter your name :")

print("Name : ",name,"( Type : ",type(name),")","( Memory Address :",id(name),")")