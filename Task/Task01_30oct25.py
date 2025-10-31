def square(num):
    if num > 0:
        return num**2
    else:
        print("only positive number allowed")

sq= square(int(input("Enter your number")))
print("square of number is:",sq)


