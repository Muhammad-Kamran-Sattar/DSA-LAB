
from funcs import RandomArray
import time
import csv




def InsertionSort(array,start,end):
    

    for i in range(start,end):
        key=array[i]
        j=i-1
        while j>=start and array[j] > key:
            array[j+1] =array[j]
            j=j-1
        array[j+1]=key 
        
    return array

n=int(input("Enter the size" ))
start_time=time.time()
start=int(input("Enter starting index:"))
end=int(input("Enter ending index:"))
array=RandomArray(n)
sortedarray= InsertionSort(array,start,end)
end_time=time.time()
runtime=end_time-start_time
filename = "sorted_array.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Index", "Value"])  # header
    for i, value in enumerate(sortedarray):
        writer.writerow([i, value])
print(sortedarray,"And time is",runtime)