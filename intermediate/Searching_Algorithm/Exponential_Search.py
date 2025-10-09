"""
Title: Additional Search Algorithms - Tutorial and Examples
Author: Python-Basics-to-Advanced Contributors
Difficulty: Intermediate
Description: Implementations and example of exponential search. Includes simple
             micro-benchmarks and practice exercises.
Date: October 2025
"""

print("=== Additional Search Algorithms Tutorial ===\n")

print("This module contains Exponential algorithms beyond binary search:")
print("Exponential search\n")

# =============================================================================
# Exponential Search
# =============================================================================

def exponential_search(arr, key):
    """Exponential search for sorted arrays. Returns index or -1."""
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == key:
        return 0
    # Find range for binary search by repeated doubling
    i = 1
    while i < n and arr[i] <= key:
        i *= 2
    # Binary search on the found range
    low = i // 2
    high = min(i, n - 1)

    # Reuse the iterative binary search
    def _bin_search(subarr, key, offset):
        l = 0
        h = len(subarr) - 1
        while l <= h:
            m = (l + h) // 2
            if subarr[m] < key:
                l = m + 1
            elif subarr[m] > key:
                h = m - 1
            else:
                return offset + m
        return -1

    return _bin_search(arr[low:high+1], key, low)


# =============================================================================
# Examples and micro-benchmark
# =============================================================================

if __name__ == "__main__":
    example = [i for i in range(0, 1000, 2)]  # even numbers 0..998
    keys = [0, 250, 999, -1]

    print("Example array: first 10 ->", example[:10])

    for k in keys:
        print(f"\nSearching for {k}:")
        print("expo_search   ->", exponential_search(example, k))

    # Simple micro-benchmark comparing linear and binary (via exponential's bin part)
    import time

    large = list(range(1000000))
    target = 999999

    start = time.perf_counter()
    lin_time = time.perf_counter() - start

    start = time.perf_counter()
    res_exp = exponential_search(large, target)
    exp_time = time.perf_counter() - start

    print(f"\nMicro-benchmark (searching present key={target}): linear={lin_time:.6f}s, exponential(binary)={exp_time:.6f}s")
