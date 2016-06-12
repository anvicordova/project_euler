tenx = 10;

def isPalindromic(number):
    decomposed_number = []
    reversed_number = []

    while (number / tenx > 0):
        pivot = number / tenx
        pivot *= tenx

        last = number - pivot
        decomposed_number.append(last)
        pivot /= tenx
        number = pivot

    decomposed_number.append(number)

    reversed_number = decomposed_number
    reversed_number = reversed_number[::-1]

    maxn = len(decomposed_number)

    for i in range(0, maxn):
        if decomposed_number[i] != reversed_number[i]:
            return False
    return True

number = range(100,1000)
number = number[::-1]

def start():
    largest = 0
    for i in number:
        update = number
        for j in update:
            result = i * j
            if isPalindromic(result):
                if(result > largest):
                    largest = result
        update.pop(update.index(i))
    return largest

print start()
