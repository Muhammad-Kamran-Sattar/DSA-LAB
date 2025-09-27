import random as rand



def RandomArray(n):
    array=[]    
    for i in range(0,n):
        r=rand.randint(0, 30000)
        array.append(r)
        
    return array
def InsertionSort(array,start,end):
    

    for i in range(start,end):
        key=array[i]
        j=i-1
        while j>=start and array[j] > key:
            array[j+1] =array[j]
            j=j-1
        array[j+1]=key 
        
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
def merge_sort(array,start,end):
    if start<end:
       mid=(start+end)//2
        
       merge_sort(array,start,mid) 
       merge_sort(array,mid+1,end)
       array= merge(array,start,mid,end)
    return array
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