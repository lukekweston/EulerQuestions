
#Create a list containing all the items
combinations = []
for a in range(2, 101):
    for b in range(2, 101):
        combinations.append(a ** b)

#getDistinct
uniqueCombinations = []
for comb in combinations:
    if(comb not in uniqueCombinations):
        uniqueCombinations.append(comb)

#print the answer
print(len(uniqueCombinations))



