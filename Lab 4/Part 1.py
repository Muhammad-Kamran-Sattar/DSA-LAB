# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 14:05:51 2025

@author: mkamr
"""

# ---- Counting Sort ----
def counting_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

arr1 = [-5, -10, 0, -3, 8, 5, -1, 10]
print("Counting Sort:", counting_sort(arr1))

# ---- Radix Sort ----
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

arr2 = [110, 45, 65, 50, 90, 602, 24, 2, 66]
print("Radix Sort:", radix_sort(arr2))

# ---- Bucket Sort ----
def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

arr3 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Bucket Sort:", bucket_sort(arr3))