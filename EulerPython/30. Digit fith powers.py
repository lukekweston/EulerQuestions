

def calc5thPower(value):
    value = str(value)
    sum = 0
    for i in value:
        sum += int(i) ** 5
    return sum


sum = 0

for i in range(1000, 200000):
    if(i == calc5thPower(i)):
        sum += i
        print(i)

print(sum)