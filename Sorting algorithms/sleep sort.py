#This implementation of the sleep sort was created by : TaxiarchisK
#github: https://github.com/TaxiarchisK
#if you want to use this implementation to you're project please link my github account
from time import sleep
import threading

a_list = [5,4,3,12,8,1]

def sleepSort(i):
    """sleep sort implementation  """
    sleep(i)                    #sleep for i seconds
    a_list.append(i)            #the smallest number will wake up faster than the bigger ones so we append it to the list



print("list before sorting : ",a_list)
threads = []
for j in range(len(a_list)):
    t = threading.Thread(target=sleepSort,args =(a_list.pop(),))   #create a new thread which calls the sleepSort funct
    #and pass list.pop() as i
    threads.append(t)                                    #add thread to threads so we can manage them
    t.start()


for i in range(len(threads)):       #wait until all threads finish so we can print the sorted list
    threads[i].join()


print("list after sorting : ",a_list)
