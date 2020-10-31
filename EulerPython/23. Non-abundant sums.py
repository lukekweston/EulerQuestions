def isAbundant(value):
    sumFactors = 1
    for i in range(2, int(value ** 0.5) + 1):
        if(int(value / i) == value / i):
            sumFactors += i
            if(value /i != i):
                sumFactors += value /i
    return sumFactors > value

abundantNumbers = []

for i in range(1, 28123):
    if isAbundant(i):
        abundantNumbers.append(i)

notTwoAbundant = [0] * (28123 + 1)

for i in range(len(abundantNumbers)):
    for j in range(len(abundantNumbers)):
        if(abundantNumbers[i] + abundantNumbers[j] > 28123):
            break
        else:
            notTwoAbundant[abundantNumbers[i] + abundantNumbers[j]] = 1

sum = 0
for i in range(len(notTwoAbundant)):
    if notTwoAbundant[i] == 0:
        sum += i

print(sum)
