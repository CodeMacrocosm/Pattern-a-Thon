def ladder_pattern(N):
    for i in range(N+1):
        print("*   *")
        print("*   *")
        if i < N:
            print("*****")

# Size of the Pattern
N = 3
ladder_pattern(N)
