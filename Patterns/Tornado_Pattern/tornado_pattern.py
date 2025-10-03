def swirling_tornado(n):
    chars = ['*', '#', '+', '~', '^', '%']
    for i in range(n, 0, -1):
        ch = chars[i % len(chars)]
        spaces = ' ' * (n - i)
        line = ch * i
        print(spaces + line)

swirling_tornado(12)
