divisors = range(11, 21) #1 to 10 included in this numbers

def divisible(number):
    for i in divisors:
        if number % i != 0:
            return False
    return True

def start():
    start = 40

    while True:
        if divisible(start):
            return start
        start += 20

print start()
