
def find_b_c(b, c):
    return 2 * b * b + 1000000 + 2 * b * c == 2 * 1000 * (b + c)


def find_a(b, c):
    return 1000 - b - c


def inRange(n):
    return n > 0 and n < 1000



def start():
    for b in range(1,1000):
        for c in range(1, 1000):
            if find_b_c(b, c):
                a = find_a(b,c)

                if inRange(a) and inRange(b) and inRange(c):
                    print a, b, c
                    return a * b* c

print start()
