rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i):
        print(" ", end="")
    
    for k in range(i, rows + 1):
        print("* ", end="")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(1, i):
        print(" ", end="")
    
    for k in range(i, rows + 1):
        print("* ", end="")
    
    print()
