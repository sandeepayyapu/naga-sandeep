
# a, b=c=7, 8
# print(a)
# print(b)
# print(c)
# a=b, c = 4, 2
#print(a, b, c)


 ----> swapping of variables
 a = 7
 b = 5

temp=a #temp=7
a=b
#a=5
b=temp #b=7
# a=5, b=7
print(a, b)

# a=a+b #a=12
# b=a-b #b=12-7=5
# a=a-b #a=12-5=7

# print(a, b)

# a, b=b, a # only in python 
# print(a, b)

#id() --> used to find the memory address of the variable
a = 7
b = 8
print(id(a))
print(id(b))

a=a*b  #a=35
b=a/b #b=35/7 =5.0
a=a/b #a=35/5 =7.0
print(int(a),int(b))

#-----> Keywords
# Keywords are reserved words which provides special meaning to # compiler or interpretor


import keyword

# print(keyword.kwlist)
# print(len(keyword.kwlist))
# print(type(keyword.kwlist))


# To check if the string is keyword or not
# print(keyword.iskeyword("sid")) # False


# if = 8
# print(if) # error coz if is a keyword

#!----> literals
# Literal is the constant value asssigned to a variable # A variable is considers to be constant when it is defines
# in caps


a= 78 # a is variable
A=78 # A is constant


#hash()  --->it creates a hash value for constant dadatypes and
# provides error for non constant dada types
n1 = 89+7j
print(hash(n1))

f1 = [7,8,9]
print(hash(f1))  # error  -->  list is  non-constant or muetable datatype



# a = 9
# b = 9
# b = 90
# print(id(a))
# print(id(b))


----> Operators
# ? Opeartors are symbols which is used to perform various opearions
# ? bewtween 2 or more operands


# Arithmatic
# Assignment
# Logical I
# Relational or comparison
# Bitwise
# Identity
# Membership


# todo
# Eg:1
# a = 8
# b = 6
# c = 9

---> Arithmatic --> +,
*, 1,%, 11,
**
# print(a+b+c)
# input() --> used to get the runtime input
# evel()--># a, b=c=7, 8
# print(a)
# print(b)
# print(c)
# a=b, c = 4, 2
#print(a, b, c)


 ----> swapping of variables
 a = 7
 b = 5

temp=a #temp=7
a=b
#a=5
b=temp #b=7
# a=5, b=7
print(a, b)

# a=a+b #a=12
# b=a-b #b=12-7=5
# a=a-b #a=12-5=7

# print(a, b)

# a, b=b, a # only in python 
# print(a, b)

#id() --> used to find the memory address of the variable
a = 7
b = 8
print(id(a))
print(id(b))

a=a*b  #a=35
b=a/b #b=35/7 =5.0
a=a/b #a=35/5 =7.0
print(int(a),int(b))

#-----> Keywords
# Keywords are reserved words which provides special meaning to # compiler or interpretor


import keyword

# print(keyword.kwlist)
# print(len(keyword.kwlist))
# print(type(keyword.kwlist))


# To check if the string is keyword or not
# print(keyword.iskeyword("sid")) # False


# if = 8
# print(if) # error coz if is a keyword

#!----> literals
# Literal is the constant value asssigned to a variable # A variable is considers to be constant when it is defines
# in caps


a= 78 # a is variable
A=78 # A is constant


#hash()  --->it creates a hash value for constant dadatypes and
# provides error for non constant dada types
n1 = 89+7j
print(hash(n1))

f1 = [7,8,9]
print(hash(f1))  # error  -->  list is  non-constant or muetable datatype



# a = 9
# b = 9
# b = 90
# print(id(a))
# print(id(b))


----> Operators
# ? Opeartors are symbols which is used to perform various opearions
# ? bewtween 2 or more operands


# Arithmatic
# Assignment
# Logical I
# Relational or comparison
# Bitwise
# Identity
# Membership


# todo
# Eg:1
# a = 8
# b = 6
# c = 9

---> Arithmatic --> +,
*, 1,%, 11,
**
# print(a+b+c)
# input() --> used to get the runtime input
# eval()--> used to get the runtime values of all data type
input("the out Enter the value: ")
n1
print (n1)input("Enter the value: ")
n1

#! //--> floor devision
# a 765433
# b = 19
# print(a//b) # -> the output will be inn integer & the output will be # based on floor value
#! ** --> used for power of a number
# print(2**4) # --> 16


# Assignment --> =+=,=, /=, =, //=, *=, &=, |=, %=
# a= 8
# a+=2
# print(a)
# a=30
# a-=5
# print(a)


# ! comparison --> == >p <, !=, <=, >=
# a = 8
# b = 7
# print (a>b) # true

# a = 9
# b = 5
# print(a==b)
# ! Bitwise operator-----> &,|,^,~,<<,>>
a = 7
b = 4
print(a&b)
<--
<<, >>


 
# 2^4 2^3 2^2 2^1 2^0
#    8       4     2        1

#    0       1     1        1       # -->  7
#    0       1      0       0       # -->  6 
# --------------------------------------------
#     0       1     1       1      #--> 1
#


 #  256  128  164
 # ! Logical operator
 # and, or, not

#a = 6
# print(a is > 3 and a is <10)
# print(a>7 or a<30)
# print(not (a>8 and a<10))


 # ! Identity operator
 #It is used to compare the memory location that the values are stored
 # is, is not
#a = 8
#b = 8
#print( a is b )
#print(a==b)

#a=[1, 2, 3]
#b=[1, 2, 3]
#print(a is b)

 #a = [1, 2, 3]
 #b = [1, 2, 3]
 #print(a is not b)

 # Membership Operator
 # in, not in
#l1 = [7, 8, 9, 0, 6, 5]
#num = 55
#print(num in l1)

#l1 = [7, 8, 9, 0, 6, 5]
#num = 55
#print(num not in l1)

 #num=678
 #print(8 in num) #error
 # ! conditional statment
  # if, elif, else

 #Eg;-1
 #--> c syntax
 # if (condition){
 #     statement;
 #     statement;
 #     statement;
 #}
 #python syntax
 # if condition:
 #    statement;
 #    statement;
 #  statement;

# Eg: 1
#a = 6
#if a:
 #   print("hello")

 #Eg:2
 #a = 6
 #if a >3:
 #print("yes")
 #else:
 #print("no")
 
#EG:3
# if 7>8:
     print("hello")



