from Tools import EratosthenesSieve as SieveOfEratosthenes

primes = SieveOfEratosthenes.primesList(2000000)


sum = 0

for p in primes:
    sum += p

print(sum)