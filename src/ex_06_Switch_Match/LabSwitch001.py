Day=int(input("Enter the number"))
match Day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case _:
        print("Invalid input")