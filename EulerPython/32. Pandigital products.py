def checkPandigital(multiplicand, multiplier, product):
    allCombined = str(multiplicand)+ str(multiplier) + str (product)
    numbersToCheck = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for n in numbersToCheck:
        if(not n in allCombined):
            return False
        elif n == "9":
            return True




sum = 0
productsFound = []
for multiplicand in range (100000):
    for multiplier in range(multiplicand, 10000):
        product = multiplicand * multiplier
        totalLength = len(str(multiplicand)) + len(str(multiplier)) + len(str(product))
        if ( totalLength > 9):
            break
        if (totalLength == 9):
            if(product not in productsFound):
                if(checkPandigital(multiplicand, multiplier, product)):
                    productsFound.append(product)
                    sum += product
                    print(sum)