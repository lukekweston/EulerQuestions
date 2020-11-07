from Tools import EratosthenesSieve as Sieve

#get all primes
primes = Sieve.primesList(1000000)
#make a boolean array of the prime numbers
primesArray = [0] * 1000000
for p in primes:
    primesArray[p] = 1
#b has to be a prime, as n starts at 0, 0 + prime has to equal prime
bList = Sieve.primesList(1000)

#keep track of the longest chain
maxCount = 0

#loop through a -999 to 999
for a in range(-999,1000):
    print(a)
    for b in bList:
        count = 0
        n = 0
        # Check if current calc is a prime
        while(primesArray[n ** 2 + a *n + b]):
            count += 1
            n += 1
        #Assign the new max if greater than the previous max chain
        if(count > maxCount):
            print(b)
            maxCount = count
            maxProduct = a * b

#print the product
print(maxProduct)

