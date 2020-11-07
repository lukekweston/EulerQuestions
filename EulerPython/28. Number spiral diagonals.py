
sum = 1
cornerValue = 1
gapBetweenValues = 2

cornersSummed = 0
while cornerValue < 1001 ** 2:
    cornersSummed += 1
    cornerValue += gapBetweenValues
    sum += cornerValue
    if(cornersSummed == 4):
        gapBetweenValues += 2
        cornersSummed = 0

print(sum)