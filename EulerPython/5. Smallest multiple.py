
def q4():
    value = 19 * 20
    while(True):
        for i in range(2,21):
            if(value % i != 0):
                break
            elif i == 20:
                return value

        value += 20 * 19
        print(value)


print(q4())


