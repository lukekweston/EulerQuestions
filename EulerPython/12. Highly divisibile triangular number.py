factors = 500

def getFactors(number):
    factors = 0
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:

            factors += 2

    return factors


def generateTriangleNumber(factors):
    i = 0
    triangle = 0
    while(True):
        i += 1
        #get the next triangle number by adding i onto it
        triangle += i
        print(triangle)
        tFactors = getFactors(triangle)
        if(tFactors  > factors):
            return triangle



print(generateTriangleNumber(factors))

import time
start_time = time.time()


def trianglenumbers(factors):
    triangle = 0
    tfact = 0
    maxfact = 0

    for numbers in range(1,100000):
        if triangle ** 0.5 == int(triangle ** 0.5): #checks to see if the number is a perfect square and subtracts 1 if it is(36 has a factor 6*6 only 1 6 should be counted though)
            tfact -= 1
        if tfact > maxfact:
             maxfact = tfact
             print(triangle,maxfact)
        tfact = 0
        triangle += numbers

        for checkfactors in range(1,int(triangle**0.5)+1): #sqrt triangle finds the limit of when factors will be repeated example 28 = 28,1 14,2 7,4 4,7 (sqrt28 =5.29... so it will stop after 7,4 and before 4,7)
            if triangle % checkfactors == 0:
                tfact +=2 #adds 2 because it finds 2 factors at a time
                if tfact > maxfactors:
                     return triangle, tfact


                #to future luke: do this with prime factors, all factors are made up of powers of primes prime1 ^ X + prime2 ^ Y ... = any number.   12 = 2 ^ 2 * 3 ^ 1 12 = 6 * 1 * 2 ^ 1also use Sieve of Eratosthenes to get the primes




maxfactors = 500

print(trianglenumbers(maxfactors))

print ("time elapsed: {:.2f}s".format(time.time() - start_time))
