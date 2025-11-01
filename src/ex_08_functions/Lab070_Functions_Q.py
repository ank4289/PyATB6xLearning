#Create a program to create a sum of three number from user input
#If user dosent enter any number ,use default as 100 ,200,300

def sum_of_three_num(a=100,b=200,c=300):
    print("Sum of the three number is ")
    return a+b+c

num1=int(input("Enter number one"))
num2=int(input("Enter number two"))
num3=int(input("Enter number three"))

if num1>0 and num2>0 and num3>0:
    Sum=sum_of_three_num(a=num1,b=num2,c=num3)
    print(Sum)
else:
    Sum=sum_of_three_num()
    print(Sum)

sum0=sum_of_three_num(10,20,30)
print(sum0)
sum1=sum_of_three_num(a=20,b=40,c=num3)
print(sum1)