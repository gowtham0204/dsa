def binarySearch(arr,low,high,x):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == x:
           return mid
        elif x > arr[mid]:
            return binarySearch(arr,mid+1,high,x)
        else:
            return binarySearch(arr,low,mid+1,x)
    else:
        return -1        

# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 40
    
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")    

