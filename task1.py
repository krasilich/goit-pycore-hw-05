from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """
    Returns a function that calculates the n-th Fibonacci number using caching.
    :return: function
    """
    cache = {}

    def fibonacci(n: int) -> int:
        if n not in cache:
            if n < 1:
                cache[n] = 0
            elif n == 1:
                cache[n] = 1
            else:
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
