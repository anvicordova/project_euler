number = 600851475143
starter_prime = 2;
prime_list = [2]
prime_factors=[]


def isPrime(number):
    for i in prime_list:
        if(number % i == 0):
            return False
    return True


if (number % 2 == 0):
    number /= 2
    prime_factors.append(2)

starter_prime = 3

while number > 1:
    pivot = starter_prime

    if(isPrime(pivot)):
        prime_list.append(pivot)

        if(number % pivot == 0):
            prime_factors.append(pivot)
            number /= pivot

    starter_prime += 2

print prime_factors[-1]
