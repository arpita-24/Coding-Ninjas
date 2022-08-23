def binarySearch(arr,l,h,key):
    if l > h:
        return -1
 
    mid = (l + h) // 2
    if arr[mid] == key:
        return mid
 
    if arr[l] <= arr[mid]:
       
        if key >= arr[l] and key <= arr[mid]:
            return binarySearch(arr, l, mid-1, key)
        return binarySearch(arr, mid + 1, h, key)
 
    if key >= arr[mid] and key <= arr[h]:
        return binarySearch(arr, mid + 1, h, key)
    return binarySearch(arr, l, mid-1, key)

def search(arr, key) :
    
    l = 0
    h = len(arr)-1
    if l > h:
        return -1
 
    mid = (l + h) // 2
    
    x = binarySearch(arr,l,h,key)
    return x
