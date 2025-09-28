import time
from funcs import InsertionSort, merge_sort, ShuffleArray

# ---------------- Read words from file ----------------
with open("D:\\3 rd semester\\DSA LAB\\DSA-LAB\\Lab 2\\words.txt", "r") as f:
    words = [line.strip() for line in f if line.strip()]

print("Total words loaded:", len(words))

# ---------------- Insertion Sort Runtime ----------------
words_copy = words[:]   # copy because sorting modifies list
start = time.time()
InsertionSort(words_copy,0,len(words)-1)
end = time.time()
print("InsertionSort Runtime (original):", end - start, "seconds")

# ---------------- Merge Sort Runtime ----------------
words_copy = words[:]
start = time.time()
merge_sort(words_copy,0,len(words)-1)
end = time.time()
print("MergeSort Runtime (original):", end - start, "seconds")

# ---------------- Shuffle ----------------
ShuffleArray(words, 0, len(words)-1)
print("\nWords shuffled!")

# ---------------- Insertion Sort After Shuffle ----------------
words_copy = words[:]
start = time.time()
InsertionSort(words_copy,0,len(words)-1)
end = time.time()
print("InsertionSort Runtime (shuffled):", end - start, "seconds")

# ---------------- Merge Sort After Shuffle ----------------
words_copy = words[:]
start = time.time()
merge_sort(words_copy,0,len(words)-1)
end = time.time()
print("MergeSort Runtime (shuffled):", end - start, "seconds")

# ---------------- Difference Observation ----------------
print("\nObservation:")
print("Insertion Sort is much slower when words are shuffled (random order).")
print("Merge Sort performs consistently well regardless of initial order.")
