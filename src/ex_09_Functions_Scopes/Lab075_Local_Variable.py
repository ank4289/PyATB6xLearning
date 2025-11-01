#Life of global variable is available everywhere
#life of local variable is available within a function
pb_global_b=12

def my_function():
    pb_a=10
    print(pb_global_b)

my_function()