# Python Program to Print parallelogram Star Pattern

rows = int(input("Enter Star Pattern Rows = "))

print("Star Pattern") 

i = rows
while(i >= 1):
    j = 1
    while(j <= i - 1):
        print(' ', end = '')
        j = j + 1

    k = 0
    while(k < rows):
        print('*', end = '')
        k = k + 1
    i = i - 1
    print()
