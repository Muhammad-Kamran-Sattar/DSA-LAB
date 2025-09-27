from funcs import RandomArray
import time
import csv
def merge_sort(array,start,end):
    if start<end:
       mid=(start+end)//2
        
       merge_sort(array,start,mid) 
       merge_sort(array,mid+1,end)
       array= merge(array,start,mid,end)
    return array
    
def merge(array,start,mid,end):
    left = array[start:mid+1]
    right = array[mid+1:end+1]

    i = j = 0
    k = start  # index for main array

# Merge elements
    while i < len(left) and j < len(right):
          if left[i] <= right[j]:
             array[k] = left[i]
             i += 1
          else:
             array[k] = right[j]
             j += 1
          k += 1

# Copy remaining elements
    while i < len(left):
          array[k] = left[i]
          i += 1
          k += 1

    while j < len(right):
          array[k] = right[j]
          j += 1
          k += 1
          
    return array
n=int(input("Enter the size" ))
start_time=time.time()
start=int(input("Enter starting index:"))
end=int(input("Enter ending index:"))
array=RandomArray(n)
sortedarray= merge_sort(array,start,end)
end_time=time.time()
runtime=end_time-start_time
filename = "SortedMergeSort.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Index", "Value"])  # header
    for i, value in enumerate(sortedarray):
        writer.writerow([i, value])
print(sortedarray,"And time is",runtime)   