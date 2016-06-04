MAX_VALUE = 4000000
f1 = 1
f2 = 2
total = 0

while f1 < MAX_VALUE and f2 < MAX_VALUE:
    if f2 % 2 == 0:
        total += f2

    f3 = f1 + f2
    f1 = f2
    f2 = f3

print total
