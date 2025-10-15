#Write a program to calculate area of circle given
#Its radius using the formula area= 3.14*r*r

Radius= float(input("Enter Radius of circle \n"))

Area=3.14*(Radius**2)

print("Area of circle is :", Area)

#String data formating
print(f"Area of circle is : {Area:.2f}")
