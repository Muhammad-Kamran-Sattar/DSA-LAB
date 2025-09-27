import time
import csv
from funcs import RandomArray
def BubbleSort(array,start,end):
    for i in range(start,end):
        swapped=False
        for j in range(0,end-i-2):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
                swapped=True
        if swapped==False:
            break
    return array
n=int(input("Enter the size" ))
start_time=time.time()
start=int(input("Enter starting index:"))
end=int(input("Enter ending index:"))
array=RandomArray(n)
sortedarray= BubbleSort(array,start,end)
end_time=time.time()
runtime=end_time-start_time
filename = "SortedBubbleSort.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Index", "Value"])  # header
    for i, value in enumerate(sortedarray):
        writer.writerow([i, value])
print(sortedarray,"And time is",runtime)