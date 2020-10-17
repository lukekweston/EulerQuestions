def primesList(maxPrime):
    primesBool = [0] * maxPrime

    for i in range(2, int(maxPrime ** 0.5)):
        if (primesBool[i] == 0):
            for j in range(i * 2, maxPrime, i):
                primesBool[j] = 1;

    primes = []

    for i in range(2,len(primesBool)):
        if primesBool[i] == 0:
            primes.append(i)

    return primes