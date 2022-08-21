def kadanes(arr):
    currSum = 0
    maxSum = 0
    for i in range(len(arr)):
        if currSum >= 0:
            currSum += arr[i]
        else:
            currSum = arr[i]
        if currSum > maxSum:
            maxSum = currSum
    return maxSum

def kadanesOfTwo(arr):
   
    narr = arr + arr
    
    return kadanes(narr)
    
def maxSubSumKConcat(arr, n, k):
	# Write your code here.
    neg = 0
    for i in arr:
        if i<0:
            neg += 1
    if neg == n:
        return max(arr)
    sm = sum(arr)
    
    if k == 1:
        return kadanes(arr)
    elif sm < 0:
        return kadanesOfTwo(arr)
    else: 
        return kadanesOfTwo(arr) + ((k-2)*sm)
