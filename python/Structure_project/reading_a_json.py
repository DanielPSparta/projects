import json

with open('Results.json', 'r') as file:        # load in json file, the r sttands for read
    numbers = json.load(file)               # stores the json file in a variable

with open('Results_in_array.json', 'r') as file:
    numbersarray = json.load(file)

with open('Dictionary_of_array.json', 'r') as file:
    Dictarray = json.load(file)

print("array of dictionaries")
for item in numbersarray:     # splits back itno individual dictionaries to iterate throguh
    print(item)
    print(item['Number1'])           # gets the value for the key Number1

print("--------------------------------------------------")
print("Dictionary of dictionaries")
Dict1 = numbers['1']
print(Dict1['Number1'])
print("--------------------------------------------------")
#print(numbers)
print("Dictionary to array")
print(Dictarray['1'])
