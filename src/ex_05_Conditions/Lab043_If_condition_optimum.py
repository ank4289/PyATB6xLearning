age= int(input("enter your age\n").strip())

print(age)

if age < 0 or age > 120:
    print("enter valid age")
else:
    if age >= 21:
        print("Allowed to go")
    else:
        print("Strictly not allowed")