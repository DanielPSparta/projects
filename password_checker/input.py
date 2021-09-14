
class Inputclass:

    def __init__(self,fname,lname,birthday,password):
        self.fname = fname
        self.lname = lname
        self.birthday = birthday
        self.password = None

    def input_fname():
        return input("What is your first name?")

    def input_lname():
        return input("What is your last name?")
