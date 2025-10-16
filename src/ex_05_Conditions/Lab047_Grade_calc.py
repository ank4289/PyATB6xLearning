""""Write a program to find grade
A-90-100
B-80-89
C-70-79
D-60-69
F-0-59

"""

marks=int(input("Enter marks\n"))

if marks >100 or marks <=-1:
    print("You can get a grade you are powefull")
else:
    if marks>=90 and marks <=100:
        print("Grade is : A")
    elif marks >=80 and marks <=89:
        print("Grade is b")
    elif marks >= 70 and marks <= 79:
        print("Grade is c")
    elif marks >= 60 and marks <= 69:
        print("Grade is D")
    elif marks >=100 and marks <-1:
        print("You can get a grade you are powefull")
    else:
        print("Grade is f")
