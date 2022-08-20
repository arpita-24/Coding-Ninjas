def flipBits(arr, n): 
    # Write your code here
    currZero = 0
    maxZero = -999
    ones = 0
    for i in arr:
        if i == 1:
            ones += 1
    if ones == len(arr):
        return len(arr)
    for i in range(len(arr)):
        if arr[i] == 1:
            currZero -=1
        else:
            currZero += 1
        maxZero = max(maxZero,currZero)
        if currZero<0:
            currZero = 0
    return ones + maxZero
