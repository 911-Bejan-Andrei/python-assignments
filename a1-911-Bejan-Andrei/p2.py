# Solve the problem from the second set here
# Problem 8
def ans(x):
    a = 1
    b = 1
    c = a + b
    while c <= n:
        a = b
        b = c
        c = a + b
    return c


n = int(input("Enter a number: "))
m = ans(n)
print("Smallest number larger than", n, "is", m)
"""
1 2 3 4 5 6  7  8  9
1 1 2 3 5 8 13 21 34
"""