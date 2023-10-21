import math

crossRows = 9
#crossRows = int(input("Enter the number of cross rows: ")) # uncomment this line for user input

if crossRows % 2 == 0:
    crossWidth = round(crossRows / 4)
    if crossWidth % 2 != 0:
        crossWidth += 1
    c1 = crossRows / 2 - crossWidth / 2
    c2 = c1 + crossWidth - 1
else:
    crossWidth = round(crossRows / 4)
    if crossWidth % 2 == 0:
        crossWidth += 1
    c1 = round(crossRows / 2 - crossWidth / 2)
    c2 = c1 + crossWidth - 1

for y in range(crossRows):
    for x in range(crossRows):
        if (c1 <= x and x <= c2) or (c1 <= y and y <= c2):
            print("x", end="")
        else:
            print(" ", end="")
    print()
