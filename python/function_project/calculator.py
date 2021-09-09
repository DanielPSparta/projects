import json


def user():
    num1 = float(input("please input the first number: "))
    num2 = float(input("please input the second number: "))
    return num1, num2

def check(num1,num2):


    print("the addition of the number: ",sum(num1,num2))
    f.write("{} + {} = {} \n".format(num1,num2,sum(num1,num2)))

    print("the subtraction of the number: ",minus(num1,num2))
    f.write("{} - {} = {} \n".format(num1,num2,minus(num1,num2)))

    print("the multiplication of the number: ",times(num1,num2))
    f.write("{} * {} = {} \n".format(num1,num2,times(num1,num2)))

    print("the division of the number: ",divide(num1,num2))
    f.write("{} / {} = {} \n".format(num1,num2,divide(num1,num2)))

    f.write("---------------------------------------------------------------\n")
    result_dict = {"Number1":num1,"Number2":num2,"Addition":sum(num1,num2),"Subtraction":minus(num1,num2),"Multiplication":times(num1,num2),"Division":divide(num1,num2)}

    return result_dict
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
#set up token for while loop, and dictionaire for loop

answer = "n"
loop_num = 1
d = {'Help':'Results are stored under the attempt in which you inputted numbers'}
#open up a file to write to
f = open("results.txt","w+")


#runs the code
while answer != "y":

    number1 ,number2 = user()
    calculation_results = check(number1,number2)

    d[loop_num] = calculation_results
    loop_num += 1
    answer = input("Are you done? (y/n) \n")
#closes the file to write to

f.close()
with open('Results.json', 'w') as file:
    json.dump(d, file, indent = 4) # the indent makes the file easier to read
