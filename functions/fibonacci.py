def fibonacci(n):
    """Return the `n`th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
