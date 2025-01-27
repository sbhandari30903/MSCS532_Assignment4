# MSCS532_Assignment4

## Heap Sort
The heap sort will sort the array by heapiying it to a max heap and swapping the first element with the last and repeating the procedire for n-1 in next itatation. As it is a inplace sorting it doesnot take extra space.
Library needed to run heap sort impletation:
    - numpy
    - matplotlib
This implementation will run the heap sort against unsorted, sorted and reverse soeted array of size 990.
This implementation will write out to a heapsort.png with the graph sowing the time taken to sort each type of array.
To run this locally go to HeapSort dir and run:
    python3 heapsort.py

## Priority Queue
The implemented data type for priority queue using max heap is python list.
The data is a task class object with attributes: task_id, priority, arrival_time, deadline
The inesrtion takes O(logn) time. After inserting at the end of the tree, it takes O(logn) time to traverse the tree to the top at worst case.
The delition also takes O(logn) time. After poping the firts element. It takes O(logn) time to heapify to max heap
The change priority task takes O(n). To change priority based on the task_it, it takes O(n) time to find the task_it and O(logn) time to create a max heap after updating priority to new value.
To run this locally go to PriorityQueue dir and run:
    python3 priorityqueue.py

Heapsort and priority queue.pdf is the analysis report.
