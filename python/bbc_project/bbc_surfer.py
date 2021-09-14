import requests

request_bbc = requests.get("https://www.bbc.co.uk")    #sends the request

print("--------------------------------status code---------------------")
print(request_bbc.status_code)   # gets the status code
input()        # pauses content press enter to continue

print("-------------------------------------content----------------------------------------")
#print(request_bbc.content)     # gets the content
