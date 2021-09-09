import json

trainee = {"fname":"Adam","lname":"smith","group": {"G1" :"ENG-94","G2":"Cyber2"},"year":2021}

print(trainee)

with open('trainee.json', 'w') as file:
    json.dump(trainee, file, indent = 4) # the indent makes the file easier to read 
