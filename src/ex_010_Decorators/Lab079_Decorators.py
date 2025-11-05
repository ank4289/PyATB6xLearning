def add_security(func):
    def wrapper():
        print("1.Start the engine")
        print("2.Check for traffic")
        print("3.Wear helmet and follow traffic rule")
        func()
        print("4.secure driving secure all the items")



    return wrapper()






@add_security
def drive_old_scooter():
    print("I am driving ola scooter")