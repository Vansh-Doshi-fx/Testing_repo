def print_reverse_star_pyramid(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

print_reverse_star_pyramid(10)