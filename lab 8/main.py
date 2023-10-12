# main.py

import random
import sorts
import time

def check_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def main():
    N = int(input("Enter the number of elements: "))
    output_file = open("output.txt", "w")

    for i in range(3):
        if i == 0:
            arr = list(range(1, N + 1))  # Sorted array
        elif i == 1:
            arr = [random.randint(1, N) for _ in range(N)]  # Random array
        else:
            arr = list(range(N, 0, -1))  # Reverse sorted array

        # Copy the original array for testing built-in sort
        arr_copy = arr.copy()

        # Perform sorting using different methods and measure execution time
        methods = [sorts.bubble_sort, sorts.shell_sort, sorts.quick_sort]
        method_names = ["Bubble Sort", "Shell Sort", "Quick Sort"]

        output_file.write(f"Number of elements: {N}\n")
        for method, method_name in zip(methods, method_names):
            arr_to_sort = arr.copy()
            start_time = time.time()
            method(arr_to_sort)
            end_time = time.time()

            is_sorted = check_sorted(arr_to_sort)
            sort_time = end_time - start_time

            output_file.write(f"Sorting method: {method_name}\n")
            output_file.write(f"Sorting successful: {is_sorted}\n")
            output_file.write(f"Execution time: {sort_time} seconds\n\n")

        # Test built-in sorting
        arr_copy_start_time = time.time()
        arr_copy.sort()
        arr_copy_end_time = time.time()
        arr_copy_sort_time = arr_copy_end_time - arr_copy_start_time

        output_file.write("Sorting method: Built-in Sort\n")
        output_file.write(f"Sorting successful: {check_sorted(arr_copy)}\n")
        output_file.write(f"Execution time: {arr_copy_sort_time} seconds\n\n")

        output_file.write("--------------------------------------------------------\n")

    output_file.close()

if __name__ == "__main__":
    main()
