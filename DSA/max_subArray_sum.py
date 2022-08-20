from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    currSum = 0
    maxSum = -999
    neg = 0
    for i in arr:
        currSum += i
        maxSum = max(currSum,maxSum)
        if currSum<0:
            currSum = 0
        if i<0:
            neg += 1
    if neg == len(arr):
        return 0
    return maxSum


#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
