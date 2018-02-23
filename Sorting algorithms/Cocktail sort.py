#this implementation of the cocktail sort can be found at: https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Cocktail_sort
def cocktailSort(a_list):       #with a little twist i added the end variable at the first for loop
    swapped = False
    end = 0
    for k in range(len(a_list)-1,end,-1):   #i noticed that if we exchange the zero with a variable that
    #gets incremented by one each time we complete both for loops inside the main for loop
    #we dont have to check numbers that have been sorted
        for i in range(k,0,-1):
            if a_list[i] < a_list[i-1]:
                a_list[i],a_list[i-1] = a_list[i-1],a_list[i] #swap a_list[i] with a_list[i+1]
                swapped = True

        for i in range(k):
            if a_list[i] > a_list[i+1]:
                a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
                swapped  = True

        end = end + 1
        if not swapped:
            return

a_list = [100,2,57,1,78,56,14,564,12,78,1236,45,77,4,846,45]
print("List before sorting : " , a_list)
cocktailSort(a_list)
print("List after sorting: " , a_list)