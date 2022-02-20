# Solve the problem from the first set here
# Problem 2
def is_prime(n):
    for i in range(2, int(n / 2)):
        if n % i == 0:
            return 0
    return 1


def goldbach(n):
    pairs = []
    for p1 in range(2, int(n / 2) + 1):
        p2 = n - p1
        if is_prime(p1) and is_prime(p2):
            element = [p1, p2]
            pairs.append(element)
    return pairs


number = int(input("Enter a number: "))
prime_pairs = goldbach(number)

print("Prime numbers with the sum of", number, " are ", prime_pairs)
