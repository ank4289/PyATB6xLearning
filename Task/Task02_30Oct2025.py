def value_of_triangle(a,b,c):

    if a==b==c:
        print("It is a equilateral triangle")
    elif a ==b or a==c or b==c:
        print("it is isoscles triangle")
    else:
        print("it is scalene triangle")

side1=int(input("Please enter side 1"))
side2 = int(input("Please enter side 2"))
side3 =int(input("Please enter side 3"))
value_of_triangle(a=side1,b=side2,c=side3)