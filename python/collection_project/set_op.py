colours = {'black','grey','red','blue','green'}
#or
items =set(("coffee","tes","soda"))    # same functions 
print(colours)

colours.add('yellow')
colours.discard('grey')

colours1 = {'black','grey','red'}
colours2 = {'balck','blue'}

colours1 & colours2           #intersect
colours1 | colours2           #union
colours1 - colours2           #differnece
colours1 > colours2           #superset
