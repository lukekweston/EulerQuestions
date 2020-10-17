
def findTripletWithValue(value):
    for a in range(int(value/2)):
        for b in range(int(value/2)):
            c = (a ** 2 + b ** 2) ** 0.5
            if(c % 1 == 0):
                if(a + b +c == value):
                    print(a, b, c)
                    print(a * b * c)
                    return


findTripletWithValue(1000)


