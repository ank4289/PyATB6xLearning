print("enter test case you want to run")
test_type= input("Enter test type")
match test_type:
    case "Api":
        print("API test using postman")

    case "selenium":
        print("Automate testing using selenium")

    case "performance":
        print("Perform testing using jmeter")

    case "security":
        print("we are running security test case")

    case _:
        print("Invalid input")