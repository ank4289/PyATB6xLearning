#find max between 3 number

num1=int(input("enter number one"))
num2=int(input("enter number two"))
num3=int(input("enter number three"))

if num1 >= num2 and num1 >= num3:
    print("MAx :",num1)
elif num2 >= num1 and num2 >= num3:
    print("Max",num2)
else:
    print("Max",num3)