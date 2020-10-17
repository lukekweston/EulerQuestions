count = 0

for i in range(1, 1000):
    for j in range(1, 100):
        if(j == len(str(i ** j))):
            print(j, len(str(i ** j)), i ,j ,i ** j)
            count += 1

print(count)