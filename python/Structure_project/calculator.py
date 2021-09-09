from calc_package import calc_module as op   # contains methods for adding, minusing, dividing and multiplication
import json                                   # methods for reading and writing to a json file

def user():
    num1 = float(input("please input the first number: "))
    num2 = float(input("please input the second number: "))
    return num1, num2

def check(num1,num2):      #adds, subtracts, divideds, and multiplies 2 numbers

    result_list = []           # making a list to store results in
    result_list.append(num1)
    result_list.append(num2)

    #prints to console and save to a txt file and append to a list
    print("the addition of the number: ",op.sum(num1,num2))
    f.write("{} + {} = {} \n".format(num1,num2,op.sum(num1,num2)))
    result_list.append(op.sum(num1,num2))
    print("the subtraction of the number: ",op.minus(num1,num2))
    f.write("{} - {} = {} \n".format(num1,num2,op.minus(num1,num2)))
    result_list.append(op.minus(num1,num2))
    print("the multiplication of the number: ",op.times(num1,num2))
    f.write("{} * {} = {} \n".format(num1,num2,op.times(num1,num2)))
    result_list.append(op.times(num1,num2))
    print("the division of the number: ",op.divide(num1,num2))
    f.write("{} / {} = {} \n".format(num1,num2,op.divide(num1,num2)))
    result_list.append(op.divide(num1,num2))
    f.write("---------------------------------------------------------------\n")

    #makes a dictionary of the results and this will be output
    result_dict = {"Number1":num1,"Number2":num2,"Addition":op.sum(num1,num2),"Subtraction":op.minus(num1,num2),"Multiplication":op.times(num1,num2),"Division":op.divide(num1,num2)}

    return result_dict , result_list
#open up a file to write to
#set up token for while loop, and dictionaire for loop

answer = "n"
loop_num = 1
d = {'Help':'Results are stored under the attempt in which you inputted numbers'} # makes a dictionary to store result dictonaries in
result_array = []         # store the results as an array of dictionaries
a = {'Help':'Dictionary of array of rsults'}
#open up a file to write to
f = open("results.txt","w+")


#runs the code
while answer != "y":

    number1 ,number2 = user()          # asks user for numbers
    calculation_results , calc_results_list = check(number1,number2)           #gets the calculations for the numbers and outputs as a dictonary

    result_array.append(calculation_results)          # appends results to an array

    a[loop_num] = calc_results_list
    d[loop_num] = calculation_results                # appends results to a dictionary key : valu pair
    loop_num += 1
    answer = input("Are you done? (y/n) \n")            # ask whether they are done with the process or not
#closes the file to write to




f.close()
with open('Results.json', 'w') as file:        # stores the dictionary of dictionary results in a json file and saves it
    json.dump(d, file, indent = 4) # the indent makes the file easier to read

with open('Results_in_array.json', 'w') as file:       # stores the dictionary array of dictionary and save them as a json file
    json.dump(result_array, file, indent = 4) # the indent makes the file easier to read

with open('Dictionary_of_array.json', 'w') as file:       # stores the dictionary array of dictionary and save them as a json file
    json.dump(a, file, indent = 4) # the indent makes the file easier to read
