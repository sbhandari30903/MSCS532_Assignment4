import time
import numpy as np
import matplotlib.pyplot as plt

#############################################################################
#creates a max haep 
#arr -> array out of which max heap is created
#arrlen -> the last element of the array till which max heap is to be created
#treeindex -> tree root below with max heap is created
def heapify(arr, arrlen, treeindex):

    largest = treeindex
    left = 2 * treeindex + 1
    right = 2 * treeindex + 2

    #check if left root exists and elemement at left index is greater than root
    if left < arrlen and arr[left] > arr[largest]:
        largest = left
    
    #check if right root exists and elemement at right index is greater than root
    if right < arrlen and arr[right] > arr[largest]:
        largest = right
    
    #if root is not the largest swap with the largest and recursively solve for affected childrens
    if treeindex != largest:
        arr[treeindex], arr[largest] = arr[largest], arr[treeindex]
        heapify(arr, arrlen, largest)

def heapsort(arr):
    #create a max heap out of original array
    for i in range(len(arr)//2-1, -1, -1):
        heapify(arr, len(arr), i)

    #swap first and last elements of an array and create max heap without soured elements
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def gettime(lis):
    t1 = time.time()
    heapsort(lis)
    t2 = time.time()
    return t2 - t1

if __name__ == "__main__":

    unsorted_array_list = np.random.randint(1, 10000, 990).tolist() 
    print("Printing first 10 elements of unsorted_array_list before and after:") 
    print(unsorted_array_list[:10]) 
    t1 = gettime(unsorted_array_list)
    print(unsorted_array_list[:10]) 
    
    sorted_array_list = np.arange(1,991).tolist()
    print("Printing first 10 elements of sorted_array_list before and after:") 
    print(sorted_array_list[:10]) 
    t2 = gettime(sorted_array_list)
    print(sorted_array_list[:10]) 
    
    reverse_sorted_array_list = np.arange(990, 0, -1).tolist()
    print("Printing first 10 elements of reverse_sorted_array_list before and after:")
    print(reverse_sorted_array_list[:10]) 
    t3 = gettime(reverse_sorted_array_list)
    print(reverse_sorted_array_list[:10])
    
    t = [t1, t2, t3]
    arrtype = ['unsorted', 'sorted', 'reverse']

    plt.figure(figsize=(8,6))
    plt.plot(arrtype, t, label='Time taken to sort different types of array')
    plt.xlabel('Array type')
    plt.ylabel('time taken')
    plt.title('Heap Sort')
    plt.legend()
    plt.savefig('heapsort.png')
    

