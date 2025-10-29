num=int(input("Please enter a number"))

fact=1
if num <=0:
    print("fact is ",fact)
else:
    for i in range(1,num+1):
        fact=fact*i

print("factorial of number is :",fact)