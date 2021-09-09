


file = open("readme.txt", "r")

data = file.read(10)

while data != '':
    print(data)
    data = file.read(10)



file = open("readme.txt", "r")
data = file.readlines()             # stores all lines as a list
data = file.readline()              # only reads one line
file.close()





try:
    with open("readme.txt", "w") as file:
        data = file.write("This is a new line")
        print(data)
except Exception as e:
    print(e)


try:
    with open("readme.txt", "w+") as file:        # read and write privaldge
        data = file.write("New line ")
        print(data)
except Exception as e:
    print(e)


try:
    with open("readme.txt", "r") as file:        #this gets rid of having to close the file at the end in finally
        data = file.write("New line ")                       # with opens a resource then closes it for you when you are finished
        print(data)
except Exception as e:
    print(e)

try:
    with open("readme.txt", "r+") as file:        #this gets rid of having to close the file at the end in finally
        data = file.write("New line ")                       # with opens a resource then closes it for you when you are finished
        print(data)
except Exception as e:
    print(e)
