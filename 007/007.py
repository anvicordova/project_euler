primes =[2]

def nth_prime(n):

    if n == 1:
        return 2

    condition = True
    pivot = 3

    while condition:

        if isPrime(pivot):
            primes.append(pivot)

        if n == len(primes):
            condition = False
            return primes[-1]

        pivot += 2


def isPrime(number):

    for i in primes:
        if number % i == 0:
            return False

    return True

print nth_prime(10001)
