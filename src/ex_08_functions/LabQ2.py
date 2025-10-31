def f1():
    print("Welcome")
    def f2():
        print("I am calling from within")
    f2()
f1()