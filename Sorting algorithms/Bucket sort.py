#This implementation of the bucket sort was created by : TaxiarchisK
#github: https://github.com/TaxiarchisK
#if you want to use this implementation to you're project please link my github account
def bucketSort(arr):
    buckets = []
    for i in range(10):
        buckets.append([])

    for i in range(len(arr)):
        h = numberOfDigits(arr[i])
        buckets[h].append(arr[i])

    for i in range(10):
        buckets[i] = insertionsort(buckets[i])

    j = 0
    for i in range(10):
        while buckets[i]:
            arr[j] = buckets[i].pop(0)
            j += 1

    return arr

def numberOfDigits(num):
    mdiv = num // 10
    mmod = mdiv % 10
    i = 1
    while mdiv != 0:
        mdiv = mdiv // 10
        mmod = mdiv % 10
        i+=1

    return i

#this implementation of the insertion sort can be found at : https://gist.github.com/basarat/3216903
def insertionsort(A):
    #we start loop at second element (index 1) since the first item is already sorted
    for j in range(1,len(A)):
        key = A[j] #The next item we are going to insert into the sorted section of the array

        i = j-1 #the last item we are going to compare to
        #now we keep moving the key back as long as it is smaller than the last item in the array
        while (i > -1) and key < A[i]: #if i == -1 means that this key belongs at the start
            A[i+1]=A[i] #move the last object compared one step ahead to make room for key
            i=i-1 #observe the next item for next time.
        #okay i is not greater than key means key belongs at i+1
        A[i+1] = key
    return A


arr = [9,5,7,3,7,5,7,2,1,3,4,5,7,9,6,10,8]
print("Sorted array :" , bucketSort(arr))





