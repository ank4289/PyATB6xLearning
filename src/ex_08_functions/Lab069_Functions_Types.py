#user defined
#They cant return>non return
#They can return something
#They have parameters
#they dont parameter /arguments

import math


result=max(3,6)
print(result)

def greet():
    print("Hello")

greet()

def greet_by_name(name):
    print(name)

greet_by_name("Ankit")

def default_param(name="Ankit"):
    print(name)

default_param("QA")
default_param()

def multiple_param(name1="A",name2="b"):
    print("MultiParam",name1,name2)

multiple_param()
multiple_param("hitesh","sarath")
multiple_param(name1="Goku",name2="Dhruv")
multiple_param(name1="Ankit")
multiple_param(name2="Ryu")

def sum_of_two_number(a=20,b=30):
    print("sum of two number is")
    return a+b

result=sum_of_two_number()
print(result)
result=sum_of_two_number(a=6,b=7)
print(result)
