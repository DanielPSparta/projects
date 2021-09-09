import json

with open('trainee.json', 'r') as file:
    trainee = json.load(file)                 #loads a json file

print(trainee)

for key, value in trainee.items():
    print(f"{key} = {value}")

trainee['year'] = [2020,2021,2022]             # replace the dictionary value

with open('trainee.json', 'w') as file:
    json.dump(trainee, file, indent = 4)            #dumps the file back. svae it
