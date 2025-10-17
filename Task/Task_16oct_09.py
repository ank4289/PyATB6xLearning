username=input("Enter user name \n")
password=int(input("Enter Password \n"))
print(type(username))
if username == "admin" and password == 1234:
    print("You have login successfully")
else:
    print("Enter correct user name and Password : Login again")