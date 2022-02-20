# Solve the problem from the third set here
# Problem 13

def solve(n):
    primes = 1
    if n == 1:
        return 1
    for element in range(1, n + 1):
        d = 2
        while element != 1:
            if element % d == 0:
                primes = primes + 1
                if primes == n:
                    return d
            while element % d == 0:
                element = element / d
            d = d + 1


number = int(input("Enter a number: "))
print("The n-th number is:", solve(number))
