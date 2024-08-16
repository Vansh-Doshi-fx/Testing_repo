import sys

def print_star_pattern(n):
    for i in range(n):
        print('* ' * (i + 1))
    print_star_pattern(n)