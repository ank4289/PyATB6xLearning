Status_Code=int(input("Enter the status code"))

def check_status(sta):
    if sta== 200:
        print("The test is Pass")
    elif sta==400 or sta ==500:
        print("The test is failed")
    else:
        print("The test is Unknown")

check_status(Status_Code)
