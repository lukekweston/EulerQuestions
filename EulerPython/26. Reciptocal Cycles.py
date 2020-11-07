from Tools import EratosthenesSieve as SieveOfEratosthenes

def reacurringLength(number):
    remainder = 10
    i = 0
    while (remainder != 10 and remainder != 0) or i < 1 :
        remainder = (remainder % number) * 10
        i += 1
    return i

primes = SieveOfEratosthenes.primesList(1000)

maxDenominatior = 0
maxReaccuringLength = 0

for i in primes[1:]:
    length = reacurringLength(i)
    if( length > maxReaccuringLength):
        maxReaccuringLength = length
        maxDenominatior = i

print(maxDenominatior)






