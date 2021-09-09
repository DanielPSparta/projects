import calculator as cal

#number1 = float(input("Plaese enter the first number: "))
#number2 = float(input("Please enter the second number: "))

#calculatorObject = cal.CalculatorClass(number1, number2)   # create an object from calculator class

#sum = calculatorObject.add() #call on calculator class object method
#minus = calculatorObject.subtract()
#times = calculatorObject.multiply()
#div = calculatorObject.divide()

#results = [sum,minus,times,div]

#print(results)
cal.CalculatorClass.op_count
loop = 1
answer = 'n'
dictofdict = {'Help':'Results are stored under the attempt in which you inputted numbers'}

while answer == 'n':
    number1 = float(input("Please enter the first number: "))
    number2 = float(input("Please enter the second number: "))
    calculatorObject = cal.CalculatorClass(number1, number2)
    result = calculatorObject.check()
    cal.CalculatorClass.op_count += 4

    answer = input('Are you done? (y/n)')
    dictofdict[loop] = result
    loop += 1
    print(cal.CalculatorClass.op_count)

print(dictofdict)


#with open('dictofdict.json', 'w') as file:        # stores the dictionary of dictionary results in a json file and saves it
#    json.dump(d, file, indent = 4) # the indent makes the file easier to read

#print(calculatorObject.check())

   #this cannot be changed within an object you have to call the class not the onject
