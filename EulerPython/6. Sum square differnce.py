def sumOfSquares(max):
    sum = 0
    for i in range(1, max +1):
        sum += i ** 2
    return sum

def squareOfSum(max):
    sum = 0
    for i in range(1, max + 1):
        sum += i
    return sum ** 2


def sumOfSquareDifference(max):
    return squareOfSum(max) - sumOfSquares(max)


print (sumOfSquareDifference(100))