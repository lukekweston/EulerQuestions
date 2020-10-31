properDivsors = {}

def getProperDivsors(value):
    sum = 1
    for i in range(2, int(value ** 0.5) + 1 ):
        if( value / i == int(value / i)):
            sum += i
            sum += value / i

    return int(sum)



for i in range(1,10000):
    properDivsors[i] = getProperDivsors(i)

sum = 0

for i in range(1,10000):
    val1 = properDivsors[i]
    if val1 in properDivsors:
        if(properDivsors[val1] == i and val1 != i):
            sum += val1
            sum += i

# divide sum by 2 because it will add both 284, 220 and 220, 284
print(sum / 2)



