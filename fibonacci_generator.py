import itertools

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def get_fibonacci_list(n):
    return list(fibonacci_sequence(n))