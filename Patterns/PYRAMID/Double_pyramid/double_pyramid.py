def double_pyramid(height: int) -> None:
    for i in range(1, height + 1):
        print(' ' * (height - i) + '*' * i, end='')
        print('  ', end='')
        print('*' * i)
double_pyramid(5)