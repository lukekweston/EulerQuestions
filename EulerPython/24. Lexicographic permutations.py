import itertools

inputNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

output = itertools.permutations(inputNumbers)

i = 0
for o in output:
    i += 1
    if(i == 1000000):
        print(o)
        break