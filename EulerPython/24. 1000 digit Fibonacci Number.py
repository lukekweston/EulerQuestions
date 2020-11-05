f1, f2 = 1, 1

#i = 1 because f1 is first index, f0 would be 0 in fibonacci sequence
i = 1

while(True):
    if(len(str(f1)) >= 1000):
        print(i)
        break
    f1, f2 = f2, f1 + f2
    i+= 1