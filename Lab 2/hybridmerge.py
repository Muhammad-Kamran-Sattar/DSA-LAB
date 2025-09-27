
from funcs import RandomArray,merge,merge_sort,InsertionSort
import time 
import csv
def hybirdmergesort(array,start,end):
    Thershold=10
    if (end-start+1)<=Thershold:
        InsertionSort(array, start, end)
    else:
        
        mid=(start+end)//2
            
        merge_sort(array,start,mid) 
        merge_sort(array,mid+1,end)
        array= merge(array,start,mid,end)
    return array
n=int(input("Enter the size" ))
start=int(input("Enter starting index:"))
end=int(input("Enter ending index:"))

array=RandomArray(n)
start_time=time.time()
sortedarray= hybirdmergesort(array,start,end)
end_time=time.time()
runtime=end_time-start_time

filename = " SortedHybridSort.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Index", "Value"])  # header
    for i, value in enumerate(sortedarray):
        writer.writerow([i, value])
print(sortedarray,"And time is",runtime) 