n = 7  
for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * i)
stem_width = n // 2
stem_height = n
for i in range(stem_height):
    print(" " * (n-1) + "*" * stem_width)
