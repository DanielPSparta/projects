#operators
sum = lambda num1, num2 : num1+num2
minus = lambda num1, num2 : num1-num2
times = lambda num1, num2 : num1*num2

#division needs exception handling

def divide(num1,num2):
    try:
        num3 = num1 /num2
    except ZeroDivisionError:
        print(ZeroDivisionError)
        return print("Not able to divide by zero")

    return num3
#set up token for while loop
