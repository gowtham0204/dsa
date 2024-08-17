def binarySearch(arr,low,high,x):
    while high >= low:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            low = mid + 1
        else:
            hight = mid - 1 
    return -1

arr = [2, 3, 4, 10, 40]
x = 2

result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")       

#time complextiy = O(logn) striver dsa example
#Auxilary Space Complexity = O(1) 
