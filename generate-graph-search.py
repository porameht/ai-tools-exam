import timeit
import random
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Generate a sorted list of integers
sorted_list = sorted(random.sample(range(1, 1000000), 100000))

# Search for a random element in the list
target = random.randint(1, 1000000)

# Measure the time taken for linear search and binary search for different list sizes
list_sizes = [1000, 5000, 10000, 50000, 100000]
linear_search_times = []
binary_search_times = []

for size in list_sizes:
    sublist = sorted_list[:size]
    linear_search_time = timeit.timeit(lambda: linear_search(sublist, target), number=1000)
    binary_search_time = timeit.timeit(lambda: binary_search(sublist, target), number=1000)
    linear_search_times.append(linear_search_time)
    binary_search_times.append(binary_search_time)

# Create line plots for time complexity
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(list_sizes, linear_search_times, marker='o', label='Linear Search', color='blue')
plt.plot(list_sizes, binary_search_times, marker='o', label='Binary Search', color='green')
plt.xlabel('List Size')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity Comparison (Myorder Exam)')
plt.legend()

# Create line plots for space complexity (assuming constant space usage for both algorithms)
plt.subplot(1, 2, 2)
space_complexity = [1] * len(list_sizes)  # Constant space for both algorithms
plt.plot(list_sizes, space_complexity, marker='o', color='red')
plt.xlabel('List Size')
plt.ylabel('Space Complexity (Constant)')
plt.title('Space Complexity Comparison (Myorder Exam)')

plt.tight_layout()
plt.show()
