# heart pattern
n = 8

# upper part of heart
for i in range(n//2, n, 2):
    for j in range(1, n-i, 2):
        print(" ", end="")
    for j in range(i):
        print('*', end="")
    for j in range(1, n-i+1, 1):
        print(" ", end="")
    for j in range(i):
        print('*', end="")
    print()

# lower part
for i in range(n, 0, -1):
    for j in range(i, n):
        print(" ", end="")
    for j in range(i*2):
        print('*', end="")
    print()
