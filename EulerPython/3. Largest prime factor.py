from Tools import EratosthenesSieve as SieveOfEratosthenes


input = 600851475143


primes = SieveOfEratosthenes.primesList(int(input ** 0.5))

factors = []

for p in primes:
    if input % p == 0:
        factors.append(p)

print("Max factor: ", factors[len(factors) -1])