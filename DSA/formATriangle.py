from sys import stdin

def possibleToMakeTriangle(arr):

    # Write your function here.
    arr.sort()
    no = 0
#     print(arr)
    for i in range(len(arr)-2):
        firstTwoSum = arr[i] + arr[i+1]
#         print(firstTwoSum,arr[i+2])
        if firstTwoSum > arr[i+2]:
            return 1
        else:
            no += 1
    if no>0:
        return 0
            

# Main code.
t = int(input().strip())

for i in range(t):
    n = list(map(int, stdin.readline().strip().split(" ")))

    if len(n) > 1:
        arr = n
    else:
        arr = list(map(int, stdin.readline().strip().split(" ")))

    if (possibleToMakeTriangle(arr)):
        print("YES")
    else:
        print("NO")
