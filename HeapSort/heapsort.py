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

if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6, 7]
    print("Original array:", sample_array)
    heapsort(sample_array)
    print("Sorted array:", sample_array)
