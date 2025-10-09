"""
Title: Binary Search - Tutorial and Examples
Author: Python-Basics-to-Advanced Contributors
Difficulty: Intermediate
Description: Iterative and recursive implementations of binary search with examples,
             doctests, performance comparison, and practice exercises.
Date: October 2025
"""

print("=== Binary Search Tutorial ===\n")

print("Binary search finds an item in a sorted list in O(log n) time.")
print("We'll provide both iterative and recursive implementations, plus examples.")

# =============================================================================
# Iterative Binary Search
# =============================================================================

def binary_search_iterative(arr, key):
    """Return the index of key in sorted list arr or -1 if not found.

    Args:
        arr (list): Sorted list of comparable items.
        key: Item to search for.

    Returns:
        int: Index of key in arr, or -1 if key is not present.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1


# =============================================================================
# Recursive Binary Search
# =============================================================================

def binary_search_recursive(arr, key, low=0, high=None):
    """Recursive binary search wrapper. Returns index of key or -1.

    This function is a small wrapper so callers can pass only arr and key.
    """
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search_recursive(arr, key, mid + 1, high)
    else:
        return binary_search_recursive(arr, key, low, mid - 1)


# =============================================================================
# Examples and doctest-like checks
# =============================================================================

example_list = [10, 20, 30, 40, 50]
print(f"Example list: {example_list}")

print("Iterative search for 40 -> expected index 3:")
print(binary_search_iterative(example_list, 40))

print("Recursive search for 40 -> expected index 3:")
print(binary_search_recursive(example_list, 40))

print("Search for missing value 25 -> expected -1:")
print(binary_search_iterative(example_list, 25))

# Edge cases
print("Edge cases:")
print("Empty list:", binary_search_iterative([], 1))
print("Single-element found:", binary_search_iterative([5], 5))
print("Single-element missing:", binary_search_iterative([5], 3))


# =============================================================================
# Performance comparison (small micro-benchmark)
# =============================================================================

import time

large_range = list(range(1000000))  # 1M items
key_present = 999999
key_absent = -1

start = time.time()
res = binary_search_iterative(large_range, key_present)
iter_time_present = time.time() - start

start = time.time()
res_rec = binary_search_recursive(large_range, key_present)
rec_time_present = time.time() - start

print(f"\nPerformance (searching present key): iterative={iter_time_present:.6f}s, recursive={rec_time_present:.6f}s")

start = time.time()
res = binary_search_iterative(large_range, key_absent)
iter_time_absent = time.time() - start

start = time.time()
res_rec = binary_search_recursive(large_range, key_absent)
rec_time_absent = time.time() - start

print(f"Performance (searching absent key): iterative={iter_time_absent:.6f}s, recursive={rec_time_absent:.6f}s")


# =============================================================================
# Practice exercises
# =============================================================================

print("\n--- Practice Exercises ---")
print("1. Modify binary search to return the insertion index (like bisect_left).")
print("2. Adapt binary search to work with a list of tuples sorted by the first element.")
print("3. Implement an iterative binary search that returns the first occurrence in a list with duplicates.")

print("\n--- End of Tutorial ---")
print("Binary search implementations and micro-benchmarks complete.")