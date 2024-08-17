def removeDuplicates(arr):
    i = 0
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
    arr1 = arr[:i+1]
    return arr1
dupList  = [1,2,3,4,4,5]
result = removeDuplicates(dupList)
print(sum)