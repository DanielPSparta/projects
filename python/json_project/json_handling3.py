import json

trainee = {"fname":"Adam","lname":"smith","group": {"G1" :"ENG-94","G2":"Cyber2"},"year":[2021,2021], "subcribed" : None, "courses" : True}
print("this is the dictionary format")
print(trainee)

print("this is the JSON object")
trainee_json_object = json.dumps(trainee)      #dumps prints the JSON object doesn't convert it
print(trainee_json_object)
