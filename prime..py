def sleve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i + i, n + 1, i):
                primes[j] = False

    for i in range(n +1):
        if primes[i]:
            print(i, end=" ")

limit = int(input("enter the limit:"))
sleve(limit)