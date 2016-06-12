n = 100

def sum_of_squares(number):
    return (number * (number + 1) * (2 * number + 1))/6

def square_of_sum(number):
    sum = number * (number + 1) / 2
    return sum * sum

result = sum_of_squares(n) - square_of_sum(n)

if(result < 0): result *= -1

print result
