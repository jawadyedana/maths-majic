def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Print only two-digit primes (10–99)
    for i in range(10, min(n + 1, 100)):
        if primes[i]:
            print(i, end=" ")

limit = int(input("Enter the limit: "))
sieve(limit)
