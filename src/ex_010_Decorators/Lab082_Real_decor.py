import time

def print_logs(func):
    def wrapper():
        print("Start of the logs")
        func()
        print("End of the logs")
    return wrapper


def time_decorator(func):
    def wrapper():
        Start_time=time.time()
        print(Start_time)
        func()
        end_time=time.time()
        print(end_time)
    return wrapper







@print_logs
@time_decorator
def test_ui():
    print("Add a function,time taken by this function 1")
    time.sleep(2)

@print_logs
@time_decorator
def test_ui_2():
    print("Add a function,time taken by this function 2")
    time.sleep(5)

test_ui()
test_ui_2()