name = {"fname":"Adam","lname":"smith","group":"ENG-94","year":2021}
#or 
name = dict(fname=Adam,lname=smith,group=ENG-94,year=2021)

print('fname: ', name['fname'])

name['fname'] = 'Daniel'

for i in name:
    print(i)

for i in name.values():
    print(i)

for key, value in name.items():
    print(key, value)
