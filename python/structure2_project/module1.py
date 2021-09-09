import module2

def welcome_module1():
    print("welcome form module1 - welcome module1 function")

if __name__='__main__':
    print("This is module 1")
    welcome_module1()
    module2.welcome_module2()

    print("This is the end of module 1")
    print(__name__)
