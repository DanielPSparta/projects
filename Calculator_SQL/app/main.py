import calculator as cal
import sqlite_functions as sq

try:   #if a table isn't made make one
    sq.make_table()
except Exception as e:
    print("Table has been made, adding to table")      # else write this




answer = 'n'       #initialisng for while loop


while answer == 'n':
    number1 = float(input("Please enter the first number: "))        #input user numbers to variables
    number2 = float(input("Please enter the second number: "))
    calculatorObject = cal.CalculatorClass(number1, number2)            #makes a calculator class object which contains number 1 and number 2
    result = calculatorObject.checklist()                                 #makes a list of results to use


    sq.table_insert(result[0],result[1],result[2],result[3],result[4],result[5])      # adds results to a database
    answer = input('Are you done? (y/n)')

sq.show_results()                                #shows the results stored in the database 
