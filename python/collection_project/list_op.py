colours = ['blue','red','black']
print(colours)
print(colours[1])

for i in colours:
    print(i)

print('blue' in colours)
colours.append('yellow')
print(colours)
colours.remove('yellow')
print(colours)

colours.sort()
print(colours)

colours.index('red')
print(colours)

print("slice", colours[0:2])
