# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 13:56:31 2025

@author: mkamr
"""
#------------------
#example 1.1
a=5
print("the value of a ",a)
#------------------
#example 1.2
a =input("Enter the value")
b=int(a)
print("Entered the value"+str(b))
#------------------
#example 1.3
array =[]
array=[1,2,3,4,5,6]
array=[[1,2,3,4,5,6],[1,2,3,4,5,6]]
#------------------
#example 1.4
array=[]
array=[ 0]*10
print(len(array))


import numpy as np
array=np.zeros(10)
print(len(array))

#------------------
#example 1.5
import random
array=[]
min=0
max=20
n=5
for i in range (0,n):
    num=random.randint(min,max)
array.append(num)
print (array)
#------------------
#example 1.6
str =["U","E","T"]
for x in range (len(str)):
     print(str[x])
     
array =[32,1,9,31,12,22] 
print(array[::-1])  

#------------------
#example 1.7
array=[1,2,3,4,5]  
arr []
#------------------
#example 1.8
given_file = open (file = 'test.txt', mode = 'r') 
lines = given_file. read () 
 
numbers = [] 
arr = lines.split() 
for s in arr: 
    num = int(s) 
    numbers.append(num) 
 
print(numbers) 
#------------------
#example 1.9
arr = ['Hello world', 'UET'] 
f = open (file="test.txt", mode="w") 
for i in arr: 
    f.write (i + "\n") 
 #------------------
 #example 1.10   
def display(arr): 
    for i in arr: 
        print(i) 
 
array = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
display(array) 

 #------------------
 #example 2.1
 sum = 0  
for i in range (11): 
    sum += i 
 
print(sum) 

def sum(n): 
    if n == 0: 
        return n  
    else:   
        return n + sum(n-1) 
print (sum (10)) 

 #------------------
 #example 2.2
 arr = [1,2,3,4,5,6,7,8,9,10] 
 
for i in arr: 
    print(i) 
    
    
def printArray (arr, start, end): 
    if start == end: 
        print(arr[start]) 
    else: 
        print(arr[start]) 
        printArray (arr, start+1, end) 
 
arr = [1,2,3,4,5,6,7,8,9,10] 
printArray (arr, 0, len(arr)-1)     


num = 2 
power = 5 
result = 1 
for i in range(power): 
    result = result * num 
 
print(result) 

def power (n, k): 
    if k == 1: 
        return n 
    else: 
        return n * power (n, k-1) 