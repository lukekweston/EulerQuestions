
f1, f2 = 0, 1

sum = 0

while f1 < 4000000:
    if( not f1 % 2):
        sum += f1
    f1, f2 = f2, f1+ f2

print(sum)

