n = 4  
width = 13  
for i in range(n):
    stars = width//2 + i*2
    spaces = (width - stars)//2
    print(' '*spaces + '*'*stars)
for i in range(n-2, -1, -1):
    stars = width//2 + i*2
    spaces = (width - stars)//2
    print(' '*spaces + '*'*stars)
