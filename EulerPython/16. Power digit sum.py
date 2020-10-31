
#this does it with python where ints can be stored to this size
def sum(value):
    value = str(value)
    sum = 0
    for i in value:
        sum += int(i)
    return sum

print(sum(2**1000))



#this method will work with any language, creates a list/array of ints and

def sumList(l):
    sum = 0
    for i in l:
        sum += int(i)
    return sum

power = 1000
value = [2]

#creates an array of 2 ** power in reverse order
for i in range(power - 1):
    for j in range(len(value) - 1, -1, -1):
        if(value[j] * 2 > 9):
            if(j + 1 == len(value)):
                value.append(int((value[j] * 2) / 10))
            else:
                value[j + 1] = value[j + 1] + int((value[j] * 2) / 10)
        value[j] = (value[j] * 2) % 10


print(sumList(value))
