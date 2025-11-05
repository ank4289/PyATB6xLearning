def before_after_ui_test(func):
    def wrapper():
        print("Wrapper Running UI code")
        func()
        print("After running UI code")
    return wrapper()






@before_after_ui_test
def test_ui():
    print("HI, i am testing a Ui test")

