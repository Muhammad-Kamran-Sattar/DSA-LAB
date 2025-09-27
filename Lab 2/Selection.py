import time
import csv
from funcs import RandomArray

def SelectionSort(array,start,end):
    for i in range(start,end):
        min_index=i
        for j  in range( i+1,end):
            if array[j]<array[min_index]:
                min_index=j
    if min_index!=i:
        temp=array[i]
        array[i]=array[min_index]
        array[min_index]=temp
    return array  
n=int(input("Enter the size" ))
start_time=time.time()
start=int(input("Enter starting index:"))
end=int(input("Enter ending index:"))
array=RandomArray(n)
sortedarray= SelectionSort(array,start,end)
end_time=time.time()
runtime=end_time-start_time
filename = "SortedSelectionSort.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Index", "Value"])  # header
    for i, value in enumerate(sortedarray):
        writer.writerow([i, value])
print(sortedarray,"And time is",runtime)