#Given a Number a number you need to calculate the factorial of that number

# 3>3*2*1=6
num=int(input("Enter a number"))
fact=1

for i in range(num,0,-1):
    fact= fact*i

print("Fact is :",fact)


