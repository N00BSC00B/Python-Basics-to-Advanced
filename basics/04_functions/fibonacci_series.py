def fibonacci(n: int) -> list:
    """Return a list containing the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


# Example usage
print(fibonacci(10))
print(fibonacci(20))
