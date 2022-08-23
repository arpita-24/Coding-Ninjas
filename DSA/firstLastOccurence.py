from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

def findFirstLastPosition(arr, n, x):
    # Write your code here.
    # Return a tuple containing two integers denoting the first and last occurrence of X.
    if x not in arr:
        return (-1,-1)
    
    first = arr.index(x)
    last = n - arr[::-1].index(x) - 1
    
    return (first,last)



# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    X = int(stdin.readline())
    return N, arr, X


tc = int(input())
while tc > 0:
    N, arr, X = takeInput()
    ans = findFirstLastPosition(arr, N, X)
    stdout.write(str(ans[0]) + " " + str(ans[1]) + "\n")
    tc -= 1
