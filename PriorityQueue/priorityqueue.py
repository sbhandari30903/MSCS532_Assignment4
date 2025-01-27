class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"

#O(logn)
def insert(heap, task):
    #adds a task at the end
    heap.append(task)
    i = len(heap) - 1
    #loops until the newly added task maintains max heap by checking if the parent priority is smaller and going up
    while i > 0 and heap[(i - 1) // 2].priority < heap[i].priority:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2

def extract_max(heap):
    if len(heap) == 0:
        return None
    max_task = heap[0]
    heap[0] = heap[-1]
    #removes the first element 
    heap.pop()
    #creates max heap with rest of the tasks based on priority
    heapify_down(heap, 0)
    return max_task

#same as heapsort make max heap based on priority from i th index O(logn)
def heapify_down(heap, i):
    size = len(heap)
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and heap[left].priority > heap[largest].priority:
        largest = left
    if right < size and heap[right].priority > heap[largest].priority:
        largest = right

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify_down(heap, largest)

#change the priority of the task based on task id O(nlogn)
def change_priority(heap, task_id, new_priority):
    #iterates over task to find id O(n)
    task_index = -1
    for i, task in enumerate(heap):
        if task.task_id == task_id:
            task_index = i
    if task_index == -1: return
    current_priority = heap[task_index].priority
    heap[task_index].priority = new_priority
    #goes up if the priority is increased
    if new_priority > current_priority:
        while task_index > 0 and heap[(task_index - 1) // 2].priority < heap[task_index].priority:
            heap[task_index], heap[(task_index - 1) // 2] = heap[(task_index - 1) // 2], heap[task_index]
            task_index = (task_index - 1) // 2
    #goes down if priority is decreased        
    elif new_priority < current_priority:
        heapify_down(heap, task_index)


def is_empty(heap):
    return len(heap) == 0

# Example usage
heap = []
insert(heap, Task(1, 5, 0, 10))
insert(heap, Task(2, 3, 1, 8))
insert(heap, Task(3, 8, 2, 6))
insert(heap, Task(4, 7, 2, 6))
insert(heap, Task(5, 9, 2, 6))

print("Heap:", heap)
change_priority(heap, 1, 1)
print("Heap after priority update:", heap)
print("Extracted:", extract_max(heap))
print("Heap after extraction:", heap)
