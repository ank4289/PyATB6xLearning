#FInd the Positive number is even or odd

num=int(input("enter a number:").strip())
""" if num >=0:
    if num %2 ==0:
        print("even")
    else:
        print("odd")
else:
    print("Negative number") """

#using turneray operator
if num >=0:
    print("even" if num%2==0 else "odd")
else:
    print("Negative value not allowed")