from Tools import EratosthenesSieve as SieveOfEratosthenes
import itertools


goal = 7

primes = SieveOfEratosthenes.primesList(1000)

for p in primes:
    plist = [i for i in str(p)]
    k =(itertools.combinations(plist))
    for j in k:
        print(p,j)