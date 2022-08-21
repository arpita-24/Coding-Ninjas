from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    
    for i in arr:
        if i == 0:
            cnt0 += 1
        elif i == 1:
            cnt1 += 1
        elif i == 2:
            cnt2 += 1
    i = 0       
    while i<n:
        if cnt0>0:
            arr[i] = 0
            cnt0 -= 1
        elif cnt1>0:
            arr[i] = 1
            cnt1 -= 1
        elif cnt2>0:
            arr[i] = 2
            cnt2 -= 1
        i += 1
    


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
