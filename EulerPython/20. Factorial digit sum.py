#python way with no stack overflow

factorial = 1
for i in range(100, 0, -1):
    factorial *= i
sum = 0
for i in str(factorial):
    sum += int(i)

print(sum)


