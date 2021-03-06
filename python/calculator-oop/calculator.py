
class CalculatorClass:
#------------------------------------------------CLASS VARIABLE---------------------------------------------------------------
    op_count = 0

#---------------------------------------------CLASS METHODS-----------------------------------------------------------------------
    def update_count(cls):              #class methods take cls
        cls.op_count +=1
        print(cls.op_count)

#----------------------------------------------------SELF VARIABLE INITIALISATION---------------------------------------------------
    def __init__(self,number1,number2):     #class constructor, the variables used all over the class, initialises variables
        self.num1 = number1                #gets number1 and places it in the self.num1
        self.num2 = number2

#-----------------------------------------------------OPERATION FUNCTION---------------------------------------------------------
    def add(self):
        self.update_count()           #add function
        return self.num1 + self.num2

    def subtract(self):
        self.update_count()
        return self.num1 - self.num2

    def multiply(self):
        self.update_count()
        return self.num1*self.num2


    def divide(self):
        self.update_count()
        try:
            num3 = self.num1 /self.num2
        except ZeroDivisionError:
            print(ZeroDivisionError)
            return print("Not able to divide by zero")

        return num3
#--------------------------------------------------------RESULT RETURN-------------------------------------------------------------------
    def check(self):                              # does the calculations and outputs them as a a dictionary
        a = CalculatorClass.add(self)            #calls the add function from the calss calculatorClass
        s = CalculatorClass.subtract(self)
        m = CalculatorClass.multiply(self)
        d = CalculatorClass.divide(self)
        result_dict = {"Number1":self.num1,"Number2":self.num2,"Addition":a,"Subtraction":s,"Multiplication":m,"Division":d}
        return result_dict                  # returns results as a dictionary



    def checklist(self):                              # does the calculations and outputs them as a list
        result_list = []
        result_list.append(self.num1)
        result_list.append(self.num2)

        a = CalculatorClass.add(self)            #calls the add function from the calss calculatorClass
        result_list.append(a)
        s = CalculatorClass.subtract(self)
        result_list.append(s)
        m = CalculatorClass.multiply(self)
        result_list.append(m)
        d = CalculatorClass.divide(self)
        result_list.append(d)

        return result_list                  # returns results as a list
