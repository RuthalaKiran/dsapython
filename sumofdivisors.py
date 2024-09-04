# find the sum of divisors for the N integer numbe
# input 6
# output : 12 (1+2+3+6)


def divisors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum = sum + i
    return sum


print(divisors(6))
