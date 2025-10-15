user_age=int(input("enter your age \n"))

if user_age >18:
    print("He can travel alone")
else:
    print("He cannot travel alone")


print("He can travel alone" if user_age >18 else "he cannot travel alone")
