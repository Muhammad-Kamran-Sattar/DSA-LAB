from funcs import RandomArray, merge_sort, InsertionSort, hybridmergesort, SelectionSort, BubbleSort
import time, csv

# Step 1: Read n values from file
with open("D:\\3 rd semester\\DSA LAB\\DSA-LAB\\Lab 2\\Nvalues.txt", "r") as f:
    n_values = [int(line.strip()) for line in f if line.strip()]  

print("Values of n from file:", n_values)

results = []
for n in n_values:
    arr = RandomArray(n)  # generate array of size n
    row = [n]

    # Insertion Sort
    a = arr.copy()
    start = time.time()
    InsertionSort(a, 0, n-1)    # check if your funcs.py expects 0,n-1
    end = time.time()
    row.append(round(end - start, 6))

    # Merge Sort
    a = arr.copy()
    start = time.time()
    merge_sort(a, 0, n-1)
    end = time.time()
    row.append(round(end - start, 6))

    # Hybrid Merge Sort
    a = arr.copy()
    start = time.time()
    hybridmergesort(a, 0, n-1)
    end = time.time()
    row.append(round(end - start, 6))

    # Selection Sort
    a = arr.copy()
    start = time.time()
    SelectionSort(a, 0, n-1)
    end = time.time()
    row.append(round(end - start, 6))

    # Bubble Sort
    a = arr.copy()
    start = time.time()
    BubbleSort(a, 0, n-1)
    end = time.time()
    row.append(round(end - start, 6))

    results.append(row)

# Step 3: Save results into CSV
header = ["Value of n", "Insertion sort (seconds)", "Merge Sort (seconds)",
          "Hybrid Merge Sort (Seconds)", "Selection Sort (Seconds)", "Bubble Sort (Seconds)"]

with open("RunTime.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(results)

print("✅ RunTime.csv created with results!")
