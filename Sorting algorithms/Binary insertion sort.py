#This implementation of the biannry insertion sort can be found at: https://www.geeksforgeeks.org/binary-insertion-sort/
def binarySearch(arr,val,start,end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1

    if start > end:
        return start

    mid=(start+end)//2

    if arr[mid] > val:
        return binarySearch(arr,val,start,mid-1)
    elif arr[mid] < val:
        return binarySearch(arr,val,mid+1,end)
    else:
        return mid

def insertionSort(arr):
    for i in range(1,len(arr)):
        val = arr[i]
        j = binarySearch(arr,val,0,i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]

    return arr


arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
print("Sorted array :" , insertionSort(arr))