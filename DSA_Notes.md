# Stacks

A Stack is a fundamental data structure that follows the LIFO (Last-In-First-Out) principle. Elements are added and removed from a designated end, similar to a pile of plates where the most recent plate is on top. This behavior makes stacks ideal for scenarios where you need to process items in the reverse order they were added.

## Understanding LIFO (Last-In-First-Out)

Imagine a stack of plates. You place a new plate on top (push operation). When you want to remove a plate, you take the one from the top (pop operation). This "last in, first out" concept is the essence of LIFO.

## Implementing Stacks in Python

There are two primary ways to implement stacks in Python:

### 1. Using Arrays

```python
class Stack:

    def __init__(self):
        self.array = []

    def push(self, item):
        return self.array.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.array.pop()

    def is_empty(self):
        return len(self.array) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.array[-1]

    def size(self):
        return len(self.array)
     
    def clear(self):
        return self.clear()
```
### Overview
The `Stack` class is defined with a `capacity` attribute to limit the maximum number of elements. An array `arr` is initialized with `None` values to represent empty slots. The `top` attribute keeps track of the index of the top element (`-1` for an empty stack). Methods like `is_empty()`, `is_full()`, `push()`, `pop()`, and `peek()` are implemented to perform basic stack operations.

### Advantages
- Fast push and pop operations (`O(1)` time complexity) due to direct array indexing.

### Disadvantages
- Fixed size can be inefficient if the number of elements is not known beforehand. Resizing the array can be cumbersome.

## Using Linked Lists

### Code Example
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top=None
    
    def is_empty(self):
        return self.top == None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        removed_node = self.top.data
        self.top = self.top.next
        return removed_node
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data
    
    def size(self):
      current_node = self.top
      size = 0
      while current_node is not None:
        size += 1
        current_node = current_node.next
      return size

    def clear(self):
        while not self.is_empty():
            self.pop()
        return "Cleared"
```
# Queues

A Queue is a linear data structure that adheres to the FIFO (First-In-First-Out) principle. Elements are added to one end (called the rear or back) and removed from the other end (called the front). Imagine a line at a store; the first person in line (front) gets served first, and new customers join the line at the back. This behavior makes queues ideal for scenarios where you need to process items in the order they were added.

## Understanding FIFO (First-In-First-Out)

Think of a queue as a line of people waiting for something. The person who joined the line first (enqueued first) will be the first to be served (dequeued first). This "first in, first out" concept is the essence of FIFO.

## Implementing Queues in Python

There are two primary ways to implement queues in Python:

### 1. Using Arrays
```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow: cannot dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("No Element: cannot peek into an empty queue")
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue.clear()
        return "Cleared"
```

### Explanation

The `Queue` class is defined with a `capacity` attribute to limit the maximum number of elements. An array `arr` is initialized with `None` values to represent empty slots. `front` and `rear` indices keep track of the queue's front and rear elements, respectively. Methods like `is_empty()`, `is_full()`, `enqueue()`, `dequeue()`, and `peek()` are implemented to perform basic queue operations.

### Advantages

- Fast enqueue and dequeue operations (O(1) time complexity) due to direct array indexing.

### Disadvantages

- Fixed size can be inefficient if the number of elements is not known beforehand. Resizing the array can be cumbersome.

## Linked List Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return
        popped_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return popped_item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.front.data
```

# Explanation

Each node in the linked list holds data and a reference to the next node. `front` points to the front node of the queue, and `rear` points to the rear node. The same methods (`is_empty()`, `enqueue()`, `dequeue()`, and `peek()`) are implemented for queue operations, but they operate on nodes instead of array indices.

# Use Cases of Queues: Real-World Applications

- **Task Scheduling**: Operating systems use queues to manage processes waiting for CPU time.
- **Printer Queues**: Documents sent to print are added to a print queue and processed in FIFO order.
- **Breadth-First Search (BFS)**: BFS algorithms use queues to explore nodes level by level.
- **Simulations**: Queues model real-world waiting lines, such as customers in a store.
- **Data Processing**: In data pipelines, queues buffer data between processing stages.
- **Message Passing**: Messages are sent and received using queues in message-oriented systems.
- **Music Players**: Playlists can be implemented as queues, playing songs in the order they were added.

# Sorting Algorithms

## Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through a list, compares adjacent elements, and swaps them if they are in the wrong order. Larger elements "bubble" up to the end of the list with each pass.

### Steps:

1. **Outer Loop**: Iterate through the list a specific number of times (n-1).
2. **Inner Loop**: In each pass, compare adjacent elements (n-i times in the worst case).
3. **Swap**: If elements are out of order, swap their positions.
4. **Repeat**: Continue iterating through the outer loop until no swaps are needed, indicating the list is sorted.
```python
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
```
## Advantages:

- Easy to understand and implement.
- Good for educational purposes.

## Disadvantages:

- Time Complexity: $$O(n^2)$$ - Inefficient for large datasets. Makes many comparisons and swaps, especially in the worst case.
- Not suitable for real-world large-scale sorting problems.

## Best for:

- Small datasets: When dealing with a relatively small number of elements, Bubble Sort can be a simple and intuitive choice.

# Selection Sort

Selection sort is a sorting algorithm that repeatedly finds the minimum (or maximum) element in the unsorted portion of the list and swaps it with the first element in that unsorted portion. This process continues until the entire list is sorted.

## Steps:

1. Iterate over the list from the beginning (i = 0) to one element before the end (i < len(list) - 1).
2. Set the current element's index (i) as the index of the minimum element (min_index).
3. Iterate through the unsorted portion of the list (starting from i + 1).
4. If a smaller element is found, update the min_index to that element's index.
5. After finding the minimum element in the unsorted portion, swap the element at the min_index with the element at the current index (i).
6. Repeat steps 1-5 until the entire list is sorted.

```python
def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[min_index], nums[j] = nums[j], nums[min_index]
    return nums
```

## Time Complexity:

- Time Complexity: $$O(n^2)$$ - Involves nested loops iterating through the list for comparisons and swaps. This makes it inefficient for large datasets.

## Advantages:

- Simple to understand and implement.
- Efficient for small datasets.
- Stable sorting algorithm (maintains the relative order of equal elements).

## Disadvantages:

- Inefficient for large datasets due to nested loops.
- Makes numerous comparisons in the worst case.

## Applications:

- Sorting small lists where simplicity is a priority.
- Real-time data processing where small chunks of data need to be sorted incrementally.

# Insertion Sort

Insertion sort is a sorting algorithm that works similarly to how you might sort playing cards in your hand. It iterates over the list, gradually building a sorted sublist at the beginning. Elements are taken from the unsorted portion and inserted into their correct positions within the sorted sublist.

## Steps:

1. Start with an empty sorted sublist (containing only the first element).
2. Iterate over the unsorted portion of the list.
3. For each element in the unsorted portion:
   - Compare it to the elements in the sorted sublist, starting from the right.
   - Shift elements in the sorted sublist one position to the right to make space for the current element if it's smaller.
   - Insert the current element into its correct position in the sorted sublist.
4. Repeat steps 2-4 until the entire list is sorted.

```python
def insertion_sort(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = 

    return nums
```

## Time Complexity:

- Average and best case: $$O(n)$$ - This occurs when the list is already partially sorted or sorted entirely.
- Worst case: $$O(n^2)$$ - This happens when the list is sorted in descending order.

## Advantages:

- Simple to understand and implement.
- Efficient for small datasets or partially sorted lists.
- Stable sorting algorithm - maintains the relative order of equal elements.

## Disadvantages:

- Inefficient for large datasets due to the nested loop structure.
- Makes numerous comparisons and swaps in the worst case.

## Applications:

- Sorting small lists where simplicity is preferred.
- Real-time data processing where small chunks of data need to be sorted incrementally.

# Merge Sort

Merge sort is a divide-and-conquer sorting algorithm that works by recursively breaking down a list into sub-lists containing a single element, then merging those sub-lists back together in a sorted order.

## Steps:

1. **Divide**: If the list has only one element, it's already sorted. Otherwise, divide the list into two roughly equal sub-lists.
2. **Conquer**: Recursively sort the two sub-lists using merge sort.
3. **Combine**: Merge the two sorted sub-lists back into a single sorted list. This merging process is crucial and ensures the final list is sorted.

## Merging:

The merge step is where the magic happens. It takes two sorted sub-lists and efficiently combines them into a single sorted list. Here's how it works:

- Compare the first elements of each sub-list.
- The smaller element is added to the final sorted list.
- Remove the added element from its sub-list.
- Repeat the comparison process with the new heads of the sub-lists.
- This continues until one sub-list is empty.
- Any remaining elements in the other sub-list are simply appended to the final sorted list (they are already sorted).

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums)//2
    left_half = nums[:mid]
    right_half = nums[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    merged_list = []
    i, j = 0, 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            merged_list.append(left_sorted[i])
            i += 1
        else:
            merged_list.append(right_sorted[j])
            j += 1
        
    merged_list.extend(left_sorted[i:])
    merged_list.extend(right_sorted[j:])

    return merged_list
```

## Time Complexity:

Merge sort has a time complexity of $$O(n \log n)$$ in both the average and worst cases. This makes it a very efficient sorting algorithm, especially for large datasets.

## Advantages:

- Efficient for large datasets ($$O(n \log n)$$ time complexity).
- Works well for linked lists (doesn't require random access).
- Stable sorting algorithm (maintains the relative order of equal elements).

## Disadvantages:

- Requires additional space for merging (can be overcome with in-place merging techniques).
- Overhead of recursion for smaller lists (insertion sort might be preferable).

## Applications:

Merge sort is a widely used sorting algorithm due to its efficiency and stability. Common use cases include sorting large datasets, sorting linked lists, and external sorting (sorting data that doesn't fit in memory).

# Quick Sort

Quick Sort is a divide-and-conquer sorting algorithm that is efficient for large datasets. It works by recursively partitioning the list into sub-lists and then sorting those sub-lists.

## Here's how it works:

1. **Divide**: Choose an element from the list, called the pivot. This can be the first, last, or any element in the list.
2. **Partition**: Rearrange the list such that all elements less than the pivot are placed before it, and all elements greater than the pivot are placed after it. The pivot itself can be placed at its final sorted position. This partitioning step is crucial for the algorithm's efficiency.
3. **Conquer**: Recursively sort the two sub-lists created by the partitioning: the sub-list containing elements less than the pivot and the sub-list containing elements greater than the pivot.

```python
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = nums[len(nums)//2]

    left =  [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + equal + quick_sort(right)
```
## Time Complexity:

- **Average and Best Case**: $$O(n \log n)$$ - This makes Quick Sort a very efficient sorting algorithm for large datasets.
- **Worst Case**: $$O(n^2)$$ - This can occur when the chosen pivot consistently ends up at the wrong end of the partitioned sub-lists.

## Advantages:

- Efficient for large datasets ($$O(n \log n)$$ average time complexity).
- Relatively simple to understand and implement.
- In-place sorting algorithm (sorts the data in the same memory location, reducing memory usage).

## Disadvantages:

- Worst-case time complexity of $$O(n^2)$$ can occur with specific data patterns.
- Additional overhead compared to simpler algorithms for smaller datasets.
- Pivot selection can impact performance. Choosing a bad pivot can lead to imbalanced sub-lists and the worst-case scenario.

## Applications:

Quick Sort is a widely used sorting algorithm due to its efficiency and in-place nature. Common use cases include sorting large datasets, sorting arrays, and sorting linked lists (with some modifications).

# Heap Sort

Heap sort is a powerful sorting algorithm that leverages the efficiency of heap data structures. Here's a breakdown of the key concepts:

## Concept

Heap sort is an in-place sorting algorithm, meaning it sorts the data within the original array without requiring additional memory. It utilizes a binary heap, a specialized tree where the root node holds the largest element (max-heap) or the smallest element (min-heap). The algorithm sorts by building a heap from the input data and then repeatedly extracting the largest element (max-heap) and placing it at the end of the sorted portion of the array. It then rebuilds the heap on the remaining elements, effectively pushing the largest element out of the heap and towards the sorted end of the array.

## Steps

1. **Heapify**: Convert the input array into a max-heap. This can be done efficiently using specialized heapify algorithms with a time complexity of $$O(n)$$.
2. **Extract Max**: Swap the root element (largest element) with the last element of the heap. This places the largest element in its final sorted position.
3. **Heapify (Again)**: Reduce the size of the heap by 1 (exclude the swapped element) and rebuild the max-heap on the remaining elements. This ensures the largest element in the remaining heap becomes the root.
4. **Repeat**: Steps 2 and 3 are repeated until the heap size becomes 1, signifying a fully sorted array.

```python
def heap_sort(data):
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

def heapify(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if n > left and data[largest] < data[left]:
        largest = left
    
    if n > right and data[largest] < data[right]:
        largest = right
    
    if largest != i:
        data[largest], data[i] = data[i], data[largest]
        heapify(data, n, largest)
```

## Complexity

Heap sort has an average and best-case time complexity of $$O(n \log n)$$, making it efficient for large datasets. The worst-case complexity remains $$O(n \log n)$$ for most implementations, but it can degrade to $$O(n^2)$$ for specific data patterns.

## Advantages

- Efficient for large datasets due to its $$O(n \log n)$$ complexity.
- In-place sorting, saving memory compared to algorithms requiring extra space.
- Works well for partially sorted data, potentially performing better than algorithms like bubble sort.

## Disadvantages

- Not as stable as some sorting algorithms (e.g., merge sort), meaning the order of equal elements might be shuffled during sorting.
- Overhead associated with maintaining the heap structure compared to simpler algorithms.

## Use Cases

Heap sort is a versatile algorithm used in various applications requiring efficient data sorting, including:
- Sorting large datasets in databases.
- Implementing priority queues where elements with higher priorities are extracted first.
- Network routing algorithms.
- Graph algorithms like finding minimum spanning trees.


# Searching

## Linear Search

Linear search, also known as sequential search, is a fundamental search algorithm that iterates through a list of elements one by one to find the target element. It's a simple and easy-to-implement approach, but its efficiency can be low for large datasets.

### Understanding Linear Search

Imagine searching for a specific book in a bookshelf. You start from one end and examine each book until you find the one you're looking for, or you reach the other end without success. This is essentially how linear search works.

### Steps involved in Linear Search:

1. Initialization: Define the list of elements to be searched and the target element to be found.
2. Iteration: Start iterating through the list, comparing each element with the target element.
3. Comparison: If a match is found (current element equals target element), return the index of the found element.
4. Continue: If no match is found, continue iterating through the list.
5. Not Found: If the entire list is traversed without finding a match, return an indication that the element is not present (e.g., -1 or None).

```python
def linear_search(data, element):
    for x in data:
        if x == element:
            return data.index(x)
    return "Element not found"
```
### Time Complexity:

- Average & Best Case: O(n). In the average and best cases, the search might find the target element in the first half of the list, resulting in linear time complexity (number of comparisons proportional to the list size n).
- Worst Case: O(n). In the worst case scenario, the target element might be at the end of the list or not present at all, requiring the search to iterate through the entire list, leading to O(n) comparisons.

### Advantages:

- Simple and easy to understand: Linear search is a very intuitive concept, making it easy to learn and implement.
- No additional data structure required: Unlike some algorithms, linear search doesn't require any special data structures, making it readily applicable to various situations.

### Disadvantages:

- Inefficient for large datasets: As the list size increases, the number of comparisons required for linear search grows linearly, making it slow for large datasets.
- Not suitable for sorted lists: Linear search doesn't take advantage of any order within the list. If the list is sorted, using a more efficient search algorithm like binary search would be preferable.

### Use Cases:

- Small datasets: When dealing with relatively small lists, linear search can be a simple and sufficient approach.
- Unsorted lists: Since linear search doesn't rely on the order of elements, it can be used for unsorted lists where other sorting-based search algorithms might not be applicable.
- Real-time search: In scenarios where immediate results are desired, and the data size is limited, linear search can be a quick way to find an element.

# Binary Search

Binary search is a much faster search algorithm compared to linear search, especially for large datasets. It leverages the fact that the list is sorted to efficiently find the target element.

## Understanding Binary Search

Imagine searching for a specific name in a phonebook. Unlike linear search, where you might start at the beginning and flip through pages one by one, binary search takes advantage of the sorted nature of the phonebook. You can start by opening the book somewhere in the middle. If the target name is alphabetically before the middle name, you know you only need to search the first half of the book. Conversely, if it's alphabetically after, you only need to search the second half. This process of halving the search space continues until the target element is found or determined to be absent.

### Steps involved in Binary Search:

1. **Initialization:** Define the sorted list of elements to be searched and the target element to be found.
2. **Set boundaries:** Set two pointers, low and high, to represent the beginning and end of the search space (initially the entire list).
3. **Iteration:** While low is less than or equal to high:
    - Calculate the mid index as the middle point between low and high.
    - Compare the target element with the element at the mid index.
    - If they are equal, the target element is found, return the mid index.
    - If the target element is less than the element at mid, update high to mid - 1 (search the left half).
    - If the target element is greater than the element at mid, update low to mid + 1 (search the right half).
4. **Not Found:** If the loop finishes without finding a match (low becomes greater than high), the target element is not present in the list.

### Implementation:

Binary search can be implemented in most programming languages using a recursive or iterative approach that keeps halving the search space based on the comparison with the middle element.

### Time Complexity:

- **Best Case:** O(1). In the best case scenario, the target element might be found in the first comparison (middle element), resulting in constant time complexity.
- **Average Case:** O(log n). On average, binary search efficiently narrows down the search space with each iteration, leading to a logarithmic time complexity (number of comparisons proportional to the logarithm of the list size n).
- **Worst Case:** O(log n). Even in the worst case (target element not present or at the beginning/end), binary search performs significantly fewer comparisons than linear search for large datasets.
```python
def binary_search(data, element):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2 
        if data[mid] == element:
            return mid
        elif data[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    return "Element not found"
```

### Advantages:

- **Highly efficient for large sorted lists:** Binary search excels at finding elements in large sorted datasets due to its logarithmic time complexity.
- **Fewer comparisons:** Compared to linear search, binary search drastically reduces the number of comparisons needed to find the target element.

### Disadvantages:

- **Requires a sorted list:** Binary search relies on the list being sorted in ascending or descending order. It won't work for unsorted lists.
- **Slightly more complex to implement:** Compared to linear search, binary search involves more logic for handling the search space and comparisons.

### Use Cases:

- **Large datasets:** Whenever you need to search through a massive sorted list of elements, binary search is the preferred choice due to its efficiency.
- **Sorted arrays:** Binary search is commonly used for searching sorted arrays in various applications.
- **Data structures:** Some data structures like balanced search trees utilize binary search principles for efficient element retrieval.

# Jump Search

Jump search is a searching algorithm for sorted arrays that offers a performance improvement over linear search but is simpler to implement compared to binary search.

## Key Points:

- Works on sorted arrays only.
- Jumps through the array instead of linearly checking every element.
- Jump size is typically the square root of the array length (sqrt(n)).
- Faster than linear search with a time complexity of O(√n).
- Performs fewer comparisons than linear search for large arrays.
- Simpler to implement than binary search.

### Steps:

1. **Calculate Jump Size:** Determine the jump distance (usually sqrt(n) where n is the array length).
2. **Jump and Check:** Start at the first element (index 0). If the element is the target element, return its index. Otherwise, jump forward by the calculated jump size.
3. **Linear Search within Block:** If the jumped element is greater than the target element, perform a linear search within the previous block (from the element before the jump to the element just jumped over) to find the target element.
4. **Repeat:** If the target element is not found in the previous block, repeat steps 2 and 3 until the array is exhausted or the target element is found.

```python
def jump_sort(data, element):
    n = len(data)
    jump = int(n ** 0.5)
    previous_jump = 0

    while data[min(jump, n) - 1] < element:
        previous_jump = jump
        jump += int(previous_jump ** 0.5)
        if data[jump] != element:
            return -1

    for i in range(previous_jump, min(jump, n)):
        if data[i] == element:
            return i

    return -1
```

### Advantages:

- More efficient than linear search for large sorted arrays.
- Easier to understand and implement compared to binary search.

### Disadvantages:

- Requires the array to be sorted.
- Performance depends on choosing the optimal jump size (square root of n is a good starting point).
- May not be as efficient as binary search for very large arrays.

### Use Cases:

- When a sorted array needs to be searched efficiently and simplicity is a factor.
- As an alternative to linear search when dealing with large datasets.

# Recursion

Recursion is a programming technique where a function calls itself directly or indirectly. It's a powerful approach for solving problems by breaking them down into smaller instances of the same problem.

## Key Principles

- **Base Case:** Every recursive function must have a base case, also known as a stopping condition. This is the simplest form of the problem that the function can solve directly, preventing infinite recursion.
- **Recursive Case:** This is where the function calls itself, but with a smaller version of the original problem as input. The function should make progress towards the base case with each recursive call.
- **State Change:** As the recursion progresses, the function's state (the data it operates on) must change in a way that moves closer to the base case. This ensures the function eventually reaches the base case and terminates.
- **Call Stack:** Recursive function calls utilize a call stack in memory. Each time the function calls itself, a new activation record is pushed onto the stack. This record stores the function's current state and local variables. When the function finishes executing, its activation record is popped off the stack.

## Common Recursive Problems

Recursion is well-suited for solving problems that can be naturally divided into self-similar subproblems. Here are some examples:

- **Fibonacci Sequence:** In this sequence, each number is the sum of the two preceding ones. A recursive function can efficiently calculate the nth Fibonacci number.
- **Tree Traversals:** Traversing trees (visiting nodes in a specific order) often involves recursive functions that explore child nodes.
- **Tower of Hanoi:** This mathematical puzzle involves moving disks between rods according to specific rules. A recursive approach can solve the puzzle efficiently.
- **Binary Search:** This search algorithm efficiently locates a target value within a sorted array by repeatedly halving the search space based on comparisons. Recursion can be used to implement binary search.
- **Merge Sort:** This divide-and-conquer sorting algorithm breaks down a list into sub-lists, sorts them recursively, and then merges them back in sorted order.

## Considerations

While recursion can make code more readable and elegant for certain problems, it can also lead to issues. Very deep recursion can cause stack overflow errors if the call stack becomes too large. Additionally, recursion can sometimes be less efficient than iterative approaches in terms of memory usage and performance.

# Linked Lists

## Singly Linked List

A singly linked list is a linear data structure where elements, called nodes, are arranged in a sequential manner. Unlike arrays, nodes in a singly linked list are not stored in contiguous memory locations. Each node consists of two parts:

- **Data:** Stores the actual information held by the node (e.g., integer, string, object).
- **Next Pointer:** A reference (link) that points to the next node in the sequence. The last node's next pointer typically points to NULL to indicate the end of the list.

### Advantages of Singly Linked Lists

- **Dynamic Size:** Unlike arrays, singly linked lists can grow or shrink in size as needed, making them suitable for scenarios where the number of elements is unknown beforehand.
- **Efficient Insertion/Deletion:** Insertion and deletion operations can be performed efficiently at any position in the list, especially at the beginning or end, as only a few pointer adjustments are required.

### Disadvantages of Singly Linked Lists

- **Random Access:** Accessing elements by index is not possible in constant time (O(1)) as in arrays. Traversal is required to reach a specific node, leading to O(n) time complexity in the worst case.
- **Memory Overhead:** Each node stores an extra pointer, leading to slightly higher memory usage compared to arrays for storing the same data.

### Operations on Singly Linked Lists

#### Traversal:

- Start from the head node (the first node in the list).
- Follow the next pointer of each node until you reach a node with a NULL pointer (the end of the list).
- During traversal, you can access and process the data stored in each node.

#### Insertion:

- Create a new node with the data you want to insert.
- There are three common insertion scenarios:
  - **At the Beginning (Head Insertion):**
    - Update the next pointer of the new node to point to the current head node.
    - Make the new node the new head of the list.
  - **At the End:**
    - Traverse the list to find the last node (the node with a NULL next pointer).
    - Update the next pointer of the last node to point to the new node.
  - **After a Specific Node:**
    - Traverse the list to find the node before the insertion point.
    - Update the next pointer of the previous node to point to the new node.
    - Update the next pointer of the new node to point to the node that was originally after the previous node.

#### Deletion:

- Find the node to be deleted (and the node before it, if applicable).
- There are two deletion scenarios:
  - **Head Deletion:**
    - Update the head pointer to point to the node that was originally after the head node.
  - **Deletion in the Middle or End:**
    - Update the next pointer of the previous node to point to the node that was originally after the node to be deleted.

#### Searching:

- Traverse the list and compare the data of each node with the search value.
- If a match is found, return the node or its index (if applicable).
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingelyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_position(self, previous_node, data):
        if not previous_node:
            print('Previous data does not exist')
            return
        node = Node(data)
        node.next = previous_node.next
        previous_node.next = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node

    def delete_head(self):
        if not self.head:
            print("Linked List is empty")
            return
        self.head = self.head.next

    def delete_data(self, data):
        if not self.head:
            print("Linked List is empty")
            return
        if self.head and self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node and current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        print("Data not found in the list")

    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
```
# Doubly Linked List

A doubly linked list (DLL) is a linear data structure where each node contains three fields:

- **Data:** The element's value being stored.
- **Next:** A reference (pointer) to the next node in the sequence.
- **Previous:** A reference (pointer) to the previous node in the sequence.

This structure allows for traversal in both forward and backward directions, making it more flexible than singly linked lists.

### Advantages of Doubly Linked Lists:

- **Bidirectional Traversal:** You can efficiently navigate the list in both forward and backward directions. This is useful for scenarios where you need to process elements in either order.
- **Efficient Deletions:** Given a node to be deleted, you can directly modify the pointers of the previous and next nodes, removing the target node efficiently.
- **Ease of Insertion:** Inserting a new node before a given node is simpler in a DLL because you have the reference to the previous node readily available.

### Disadvantages of Doubly Linked Lists:

- **More Memory Usage:** Each node in a DLL requires additional space to store the previous pointer compared to singly linked lists.
- **Overhead in Certain Operations:** Adding or removing nodes might involve updating more pointers compared to singly linked lists.

### Use Cases of Doubly Linked Lists:

- **Cache Implementation:** Doubly linked lists are well-suited for implementing cache data structures like LRU (Least Recently Used) cache, where elements can be easily removed from either end.
- **Undo/Redo Functionality:** In text editors or drawing applications, DLLs can be used to maintain a history of actions, enabling undo/redo operations.
- **Music Player Playlist:** DLLs can efficiently manage playlists where songs can be added, removed, or rearranged in either direction.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def forward_traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def backward_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev
    
    def is_empty(self):
        return self.head == None
    
    def insert_at_beginning(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def insert_at_position(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        node = Node(data)
        node.next = prev_node.next
        node.prev = prev_node
        if prev_node.next is not None:
            prev_node.next.prev = node
        prev_node.next = node
        if self.tail == prev_node:
            self.tail = node
    
    def insert_at_end(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    
    def delete_at_beginning(self):
        if self.is_empty():
            print("Linked list is empty")
            return
        current_node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        del current_node
    
    def delete_at_end(self):
        if self.is_empty():
            print("Linked list is empty")
            return
        current_node = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        del current_node
    
    def delete_node(self, node):
        if self.head == node:
            self.delete_at_beginning()
        elif self.tail == node:
            self.delete_at_end()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            del node
    
    def search_forward(self, element):
        current_node = self.head
        while current_node:
            if current_node.data == element:
                return True
            current_node = current_node.next
        return False
    
    def search_backward(self, element):
        current_node = self.tail
        while current_node:
            if current_node.data == element:
                return True
            current_node = current_node.prev
        return False
```
# Circular Linked List

A circular linked list is a variation of a linked list where the last node points back to the first node, creating a circular structure. This differs from a traditional linked list where the last node typically points to NULL. Here are some key points to remember:

## Structure:

- Similar to a regular linked list, each node contains data and a pointer (next).
- In a circular linked list, the next pointer of the last node points back to the first node, forming a loop.
- There's no designated "head" or "tail" since you can traverse the list starting from any node.

## Types:

- **Singly Circular Linked List:** Each node has only a next pointer.
- **Doubly Circular Linked List:** Each node has a next pointer and a prev pointer for bi-directional traversal.

## Properties:

- **No Pointers to NULL:** Unlike regular linked lists, there are no NULL pointers in the circular structure.
- **Continuous Traversal:** You can start traversing from any node and keep iterating until you reach the starting node again.

## Operations:

- **Insertion:** Similar to regular linked lists, nodes can be inserted at the beginning, end, or after/before a specific node. The specific implementation may vary depending on the chosen insertion point.
- **Deletion:** Deleting a node involves adjusting the pointers of surrounding nodes to bypass the target node and maintain the circular structure.
- **Searching:** Traversal is necessary to search for elements. You can start from any node and keep iterating until you find the target element or complete a full loop without finding it.

## Advantages:

- **Efficient Insertion/Deletion at Specific Points:** In some cases, insertion or deletion can be faster than singly linked lists, especially when modifying nodes within the circular structure.
- **Memory Management:** No need for special markers like NULL at the end, potentially saving a little space.

## Disadvantages:

- **Traversal Complexity:** Traversal might require additional checks to avoid infinite loops, especially during search operations.
- **Less Common:** Compared to singly linked lists, circular linked lists are used in specific scenarios.

## Use Cases:

- **Circular Buffer:** Circular linked lists are ideal for implementing circular buffers where data overwrites the oldest elements when the buffer reaches capacity.
- **Josephus Problem:** This classic algorithmic problem can be efficiently solved using a circular linked list.
- **Undo/Redo Systems (Specific Implementations):** While doubly linked lists are more common for undo/redo, circular linked lists can be used in certain implementations.
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.head.next = self.head
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = node
            node.next = self.head

    def delete(self, data):
        if not self.head:
            print("Circular linked list is empty")
            return

        current_node = self.head
        prev_node = None
        while current_node.next != self.head:
            if current_node.data == data:
                if not prev_node:
                    self.head = current_node.next
                else:
                    prev_node.next = current_node.next
                current_node.next = None
                return
            prev_node = current_node
            current_node = current_node.next

        if current_node.data == data:
            self.head = None

    def traverse(self):
        if not self.head:
            print("Circular linked list is empty")
            return
        current_node = self.head
        while current_node.next != self.head:
            print(current_node.data)
            current_node = current_node.next

    def search(self, element):
        if not self.head:
            print("Circular linked list is empty")
            return
        current_node = self.head
        while current_node.next != self.head:
            if current_node.data == element:
                print(f"Found {element}")
                break
            current_node = current_node.next
```

# Trees

Trees are a fundamental data structure in computer science, resembling the hierarchical structure of trees found in nature. They are used to organize and efficiently access information.

## Definition

A tree is a hierarchical data structure that simulates a tree structure commonly found in nature. It consists of nodes connected by edges.

- **Nodes:** Represent elements in the tree and contain data.
- **Edges:** Connect nodes, establishing parent-child relationships.

## Characteristics

- **Root Node:** The topmost node with no parent.
- **Parent Node:** A node connected to one or more child nodes by a directed edge pointing downwards.
- **Child Node:** A node connected to a single parent node by a directed edge pointing upwards.
- **Leaf Node:** A node with no child nodes.
- **Degree:** The number of child nodes a node has.

## Types of Trees

- **Binary Tree:** Each node can have at most two child nodes.
  - **Full Binary Tree:** Every node except leaves has two child nodes.
  - **Complete Binary Tree:** All levels are completely filled except possibly the last level, which has all nodes filled to the left.
- **N-ary Tree:** Each node can have any number of child nodes (greater than two).

## Operations on Trees

- **Traversal:** Visiting each node in the tree exactly once according to a specific order.
  - **Preorder Traversal:** Visit the root, then its children from left to right.
  - **Inorder Traversal:** Visit the left subtree, then the root, then the right subtree.
  - **Postorder Traversal:** Visit the left subtree, then the right subtree, then the root.
  - **Level Order Traversal:** Visit nodes level by level from left to right.
- **Searching:** Finding a specific node with a particular value.
- **Insertion:** Adding a new node to the tree while maintaining its structure.
- **Deletion:** Removing a node from the tree while preserving its integrity.
- **Finding Maximum/Minimum Value:** Finding the node with the maximum or minimum value.
- **Finding Height/Depth:** Calculating the maximum distance from the root to the furthest leaf node.
- **Checking Balance:** Checking if the tree is balanced, i.e., the difference in height of left and right subtrees for every node is not more than 1.
- **Finding Parent:** Finding the parent node of a given node.
- **Finding Successor/Predecessor:** For a given node, finding the next higher or lower node in the tree.

## Applications of Trees

- **File Systems:** Organizing files and directories in a hierarchical structure.
- **Binary Search Trees (BST):** Efficient searching and sorting of data.
- **Trie:** Data structure for storing associative arrays and performing pattern matching.
- **Syntax Trees:** Representing the structure of code or expressions.
- **Game Trees:** Representing possible moves and outcomes in games like chess.
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            if data < current.data:
                if not current.left:
                    current.left = node
                    return
                else:
                    current = current.left
            elif data > current.data:
                if not current.right:
                    current.right = node
                else:
                    current = current.right
            else:
                return

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def preorder(self, node):
        if not node:
            return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if not node:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)
```
## Operations on Trees
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTreeOperations:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
            return
        current = self.root
        while True:
            if data < current.data:
                if not current.left:
                    current.left = node
                    return
                else:
                    current = current.left
            elif data > current.data:
                if not current.right:
                    current.right = node
                    return
                else:
                    current = current.right
            else:
                return

    def search(self, element):
        current = self.root
        while current:
            if element == current.data:
                return current
            elif element < current.data:
                current = current.left
            else:
                current = current.right
        return

    def find_min(self, node):
        if not node:
            return
        current = node
        while current.left:
            current = current.left
        return current.data

    def find_max(self, node):
        if not node:
            return
        current = node
        while current.right:
            current = current.right
        return current.data

    def height(self, node):
        if not node:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def balance(self, node):
        if not node:
            return True
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return (left_height - right_height) <= 1 and self.balance(node.left) and self.balance(node.right)

    def find_parent(self, element, node, parent=None):
        if not node:
            return None
        if element == node.data:
            return parent
        return self.find_parent(element, node.left, node) or self.find_parent(element, node.right, node)

    def find_predecessor(self, element):
        current = self.search(element)
        if not current:
            return None
        if current.left:
            return self.find_max(current.left)
        else:
            predecessor = None
            parent = self.root
            while parent != current:
                if element > parent.data:
                    predecessor = parent
                    parent = parent.right
                else:
                    parent = parent.left
            return predecessor.data

    def find_successor(self, element):
        current = self.search(element)
        if not current:
            return None
        if current.right:
            return self.find_min(current.right)
        else:
            successor = None
            parent = self.root
            while parent != current:
                if element < parent.data:
                    successor = parent
                    parent = parent.left
                else:
                    parent = parent.right
            return successor.data
```
# Heaps and Priority Queues

## Introduction
- Heaps and priority queues are closely related data structures often used to implement each other.
- A heap is a specialized tree-based data structure that satisfies the heap property.
- A priority queue is an abstract data type that allows for the management of a set of elements each with an associated value called a priority.

## Binary Heap
- A binary heap is a common implementation of a heap.
- It is a complete binary tree that satisfies the heap property.
- Two types of binary heaps:
  - Min-heap: The value of each node is greater than or equal to the value of its parent, with the minimum-value element at the root.
  - Max-heap: The value of each node is less than or equal to the value of its parent, with the maximum-value element at the root.
- Example of a min-heap:
```
      10
     /  \
    15   30
   / \   /
  40 50 100
```

## Priority Queue
- In a priority queue, elements are typically added with an associated priority.
- Basic operations include:
  - Inserting a new element
  - Removing the element with the highest priority (in a max-heap) or the lowest priority (in a min-heap).

## Heap Operations
- Insert (Add):
  - Adds a new element to the heap.
  - Add the new element to the bottom level of the heap at the leftmost open space (maintaining the complete tree property).
  - "Heapify up" by comparing the added element with its parent and swapping if necessary (to maintain the heap property). Continue until the heap property is restored.
- Extract Min/Max (Poll):
  - Removes and returns the minimum element in a min-heap or the maximum element in a max-heap.
  - Replace the root of the heap with the last element on the last level.
  - "Heapify down" by comparing the new root with its children and swapping it with the smaller (in min-heap) or larger (in max-heap) child. Repeat until the heap property is restored.
- Peek:
  - Returns the minimum or maximum element without removing it.
- Heapify:
  - Converts an unordered array into a heap.
  - Start from the first index which has a child (the last parent node) and perform "heapify down" to ensure each subtree satisfies the heap property. Repeat for all nodes above it in reverse level order.
- Increase Key/Decrease Key (Update):
  - Increases or decreases the value of an element.
  - After changing the value, depending on whether it's a min-heap or max-heap, the element is "heapified up" or "heapified down" to restore the heap property.
- Delete:
  - Removes an arbitrary element from the heap.
  - Replace the element to be deleted with the last element in the heap.
  - Perform "heapify down" or "heapify up" as required to maintain the heap property.

## Complexity
- Time complexity for the main heap operations:
  - Insert: O(log n)
  - Extract Min/Max: O(log n)
  - Peek: O(1)
  - Heapify: O(n)
  - Increase Key/Decrease Key: O(log n)
  - Delete: O(log n)

## Use Cases of Binary Heap

1. **Priority Queues**: Binary heaps are often used to implement priority queues, which are data structures that allow efficient access to the element with the highest (or lowest) priority. This is useful in many algorithms and systems that require handling tasks or data with different priorities, such as scheduling processes in operating systems, pathfinding algorithms in AI and games, and event-driven simulations.

2. **Heap Sort**: Heap sort is a comparison-based sorting algorithm that uses a binary heap to sort elements. It first builds a max-heap from the input data, then repeatedly extracts the maximum element from the heap and puts it at the end of the sorted section of the array. Heap sort has a time complexity of O(n log n), which makes it efficient for sorting large datasets.

3. **Graph Algorithms**: Binary heaps are used in famous graph algorithms like Dijkstra's algorithm and Prim's algorithm for finding the shortest path and minimum spanning tree respectively. These algorithms need to efficiently find the smallest edge from a set of edges, which can be done using a binary heap.

4. **K'th Largest/Smallest Element**: Binary heaps can be used to efficiently find the k'th largest or smallest element in an array. This can be done by building a min-heap or max-heap of size k from the array, then iterating over the rest of the array and replacing the top of the heap if a larger or smaller element is found.

5. **Median Finding**: Binary heaps can be used to efficiently find the median of a set of numbers. This can be done by maintaining two heaps, a max-heap for the numbers less than the current median, and a min-heap for the numbers greater than the current median.

## Implementation
- A binary heap can be efficiently implemented using an array.
- For a node at index i:
  - Its children are at indices 2*i + 1 and 2*i + 2.
  - Its parent is at index (i - 1) / 2.
- This structure efficiently utilizes space and allows for quick operations without the need for pointers.
## BinaryHeap Class

### Initialization

- Initialize an empty list `heap` to store the elements of the binary heap.
- Set the `min_heap` flag to determine if it's a min-heap (default) or a max-heap.

### Size

- Return the size of the binary heap by returning the length of the `heap` list.

### Parent, Left, and Right

- Calculate the index of the parent, left child, and right child of a given index using the formulas:
    - Parent: `(index - 1) // 2`
    - Left child: `(2 * index) + 1`
    - Right child: `(2 * index) + 2`

### Peek

- If the heap is empty, return `None`.
- Otherwise, return the root element of the heap, which is the first element of the `heap` list.

### Insert

- Append the new element to the end of the `heap` list.
- Call the `heapify_up` function to restore the heap property starting from the newly inserted element.

### Compare

- Compare two elements at given indices based on the type of heap (min-heap or max-heap).
- Return `True` if the element at `index` is smaller (for min-heap) or larger (for max-heap) than the element at `parent_index`.

### Swap

- Swap the elements at the given indices in the `heap` list.

### Heapify Up

- While the current `index` is greater than 0 and the element at the current `index` is smaller (for min-heap) or larger (for max-heap) than its parent:
    - Swap the element at the current `index` with its parent.
    - Update the current `index` to the parent `index`.

### Remove

- If the heap is empty, return `None`.
- Store the root element (first element) of the heap.
- If the size of the heap is greater than 1:
    - Replace the root element with the last element of the heap.
    - Remove the last element from the heap.
    - Call the `heapify_down` function to restore the heap property starting from the root.
- Otherwise, remove the only element from the heap.
- Return the stored root element.

### Has Left and Has Right

- Check if the left or right child of a given `index` exists by comparing the calculated left or right `index` with the size of the heap.

### Heapify Down

- While the current `index` has a left child:
    - Get the `index` of the child with the smaller (for min-heap) or larger (for max-heap) value using the `get_child_index` function.
    - If the element at the child `index` is not smaller (for min-heap) or larger (for max-heap) than the element at the current `index`, break the loop.
    - Swap the element at the current `index` with the element at the child `index`.
    - Update the current `index` to the child `index`.

### Get Child Index

- If the right child exists and is smaller (for min-heap) or larger (for max-heap) than the left child, return the `index` of the right child.
- Otherwise, return the `index` of the left child.

### Increase Key and Decrease Key

- If the given `index` is out of range or the new value is invalid (smaller for increase key or larger for decrease key), raise a `ValueError`.
- Update the value at the given `index` with the new value.
- Call `heapify_up` for increase key or `heapify_down` for decrease key to restore the heap property.

### Delete

- If the given `index` is out of range, raise a `ValueError`.
- Replace the element at the given `index` with the last element of the heap.
- Remove the last element from the heap.
- If the `index` is within the range of the heap:
    - If the `index` is 0 or the element at the `index` is smaller (for min-heap) or larger (for max-heap) than its parent, call `heapify_up`.
    - Otherwise, call `heapify_down`.

```python
class BinaryHeap:
    def __init__(self, min_heap=True):
        self.heap = []
        self.min_heap = min_heap

    def size(self):
        return len(self.heap)
    
    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return (2 * index) + 1

    def right(self, index):
        return (2 * index) + 2

    def peek(self):
        if not self.heap:
            return None
        else:
            return self.heap[0]

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(self.size() - 1)

    def compare(self, index, parent_index):
        if index >= self.size() or parent_index >= self.size():
            return False
        if self.min_heap:
            return self.heap[index] < self.heap[parent_index]
        else:
            return self.heap[index] > self.heap[parent_index]

    def swap(self, index, parent_index):
        self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

    def heapify_up(self, index):
        while index > 0 and self.compare(index, self.parent(index)):
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def remove(self):
        if not self.heap:
            return None
        root = self.heap[0]
        if self.size() > 1:
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.heapify_down(0)
        else:
            self.heap.pop()
        return root

    def has_left(self, index):
        return self.left(index) < self.size()

    def has_right(self, index):
        return self.right(index) < self.size()

    def heapify_down(self, index):
        while self.has_left(index):
            child_index = self.get_child_index(index)
            if not self.compare(child_index, index):
                break
            self.swap(index, child_index)
            index = child_index

    def get_child_index(self, index):
        if self.has_right(index) and self.compare(self.right(index), self.left(index)):
            return self.right(index)
        return self.left(index)

    def increase_key(self, index, new_value):
        if index >= self.size() or new_value < self.heap[index]:
            raise ValueError("Invalid index or new value")
        self.heap[index] = new_value
        self.heapify_up(index)

    def decrease_key(self, index, new_value):
        if index >= self.size() or new_value > self.heap[index]:
            raise ValueError("Invalid index or new value")
        self.heap[index] = new_value
        self.heapify_down(index)

    def delete(self, index):
        if index >= self.size():
            raise ValueError("Invalid index range")
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        if index < self.size():
            if index == 0 or self.compare(index, self.parent(index)):
                self.heapify_up(index)
            else:
                self.heapify_down(index)
```
# Priority Queues

A **priority queue** is a specialized type of queue that organizes elements based on their priority values. Unlike a regular queue, where elements are processed in the order they were added, a priority queue ensures that elements with higher priority values are dequeued before those with lower priority values.

## Key Points about Priority Queues

### Priority Assignment

- Each element in a priority queue has an associated priority value.
- When you add an element to the queue, it is inserted in a position based on its priority value.
- Higher-priority elements are served first.

### Implementation Methods

Priority queues can be implemented using various data structures, including:

- Arrays
- Linked lists
- Heaps (e.g., binary heaps)
- Binary search trees

## Use Cases

Priority queues find applications in scenarios where the order of processing matters significantly:

- **Real-Time Systems**: In systems where timely execution is crucial (e.g., task scheduling, process management), priority queues ensure that high-priority tasks are handled promptly.
- **Graph Algorithms**:
    - **Dijkstra’s Algorithm**: Used for finding the shortest path in a graph. Time complexity varies based on the implementation ($O(V^2)$ with arrays, $O((V+E)\log V)$ with a priority queue).
    - **A* Search Algorithm**: Used for pathfinding. It combines the advantages of both Dijkstra’s algorithm and greedy best-first search.
- **Job Scheduling**: Prioritizing tasks based on urgency or importance.
- **Network Routing**: Ensuring efficient data packet routing.

## Time Complexity

- Enqueuing and dequeuing in a priority queue (implemented as a binary heap) have a worst-case time complexity of $O(\log n)$, where $n$ is the number of elements.
- Peeking (looking at the highest-priority element) is an efficient $O(1)$ operation.

## Array-Based Implementation

One straightforward way to implement a priority queue is by using an array. However, this approach has limitations, such as high memory consumption and complexity.
```python
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self) == 0

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def peek_max(self):
        if self.is_empty():
            raise Exception("Priority queue is empty")
        return self.heap[0]

    def extract_max(self):
        if self.is_empty():
            raise Exception("Priority queue is empty")
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if not self.is_empty():
            self.heapify(0)
        return root

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        self.heapify(index)

    def delete(self, value):
        if self.is_empty():
            raise Exception("Priority queue is empty")
        index = self.heap.index(value)
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        if not self.is_empty():
            self.heapify(index)

    def heapify(self, index):
        largest = index
        left = self.left(index)
        right = self.right(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(largest)
```

# Hash Tables

Hash tables are data structures that efficiently store data with unique keys using a hash function.

## Hashing Functions

A hashing function processes an input key to produce an index in an array, known as a hash table. This index is referred to as the hash index. Common hashing functions include:

- **Division Method**: `hash(key) = key % table_size`
- **Multiplication Method**: `hash(key) = floor(table_size * (key * A % 1))`, where `A` is a constant between 0 and 1.
- **Universal Hashing**: Utilizes a family of hash functions, selecting one at random.

## Collision

Collisions occur when multiple keys produce the same hash index. This can happen if the hash function assigns the same hash value to different keys.

## Collision Resolution Strategies

To handle collisions, several strategies are employed:

- **Separate Chaining**: Each cell in the hash table points to a linked list of records with the same hash function value.
- **Open Addressing**:
  - **Linear Probing**: Searches linearly for an empty cell following a collision.
  - **Quadratic Probing**: Adds successive values of a quadratic polynomial to the original hash index until an empty slot is found.
  - **Double Hashing**: Uses a secondary hash function to find an empty slot.
  - **Coalesced Hashing**: Combines separate chaining and open addressing.
  - **Cuckoo Hashing**: Employs two hash functions, ensuring two possible places for each key/value pair.
  - **Robin Hood Hashing**: Minimizes the maximum displacement of a key from its original position.
  - **2-choice Hashing**: Uses two hash functions, placing each new key in the less loaded of two buckets.

## Probe Sequence

The probe sequence is the order of slots checked during key insertion or lookup, varying with the collision resolution strategy.

## Time Complexities

- **Average and Best Case**: O(1), indicating constant time operations for insertion, lookup, and deletion.
- **Worst Case**: O(n), occurring when many elements hash to the same key or when rehashing is necessary.

## Operations

- **Set (Insert/Update)**: Adds or updates a key-value pair.
- **Get (Lookup)**: Retrieves the value for a specific key.
- **Delete**: Removes a key-value pair.

## Use Cases

- **Databases**: Essential for data storage and retrieval, caching, and indexing.
- **Caching**: Enhances data retrieval speed.
- **Symbol Tables**: Links identifiers to values in programming.
- **Network Routing**: Optimizes data packet paths.
- **Data Compression**: Facilitates faster string searching.
## Simple Implementation

The collisions are handeled automatically.

```python
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, None)

    def remove(self, key):
        if key in self.table:
            value = self.table[key]
            del self.table[key]
            return value
        return None

    def clear(self):
        self.table.clear()
```
## Classic Implementation
```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def _hash(self, key):
        hash_key = sum(ord(char) for char in str(key)) % self.capacity
        return hash_key

    def insert(self, key, value):
        index = self._hash(key)
        node = Node(key, value)
        if not self.table[index]:
            self.table[index] = node
        else:
            head = self.table[index]
            while head.next:
                head = head.next
            head.next = node
        self.size += 1
        if self.size > self.capacity * 0.7:
            self._resize(self.capacity * 2)

    def get(self, key):
        index = self._hash(key)
        head = self.table[index]
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def _resize(self, new_capacity):
        old_table = self.table
        self.capacity = new_capacity
        self.table = [None] * self.capacity
        self.size = 0
        for head in old_table:
            while head:
                self.insert(head.key, head.value)
                head = head.next

    def remove(self, key):
        index = self._hash(key)
        head = self.table[index]
        prev = None
        while head:
            if head.key == key:
                if not prev:
                    self.table[index] = head.next
                else:
                    prev.next = head.next
                self.size -= 1
                return head.value
            prev = head
            head = head.next
        return None

    def clear(self):
        self.table = [None] * self.capacity
        self.size = 0
```
# AVL Trees

AVL Trees, named after their inventors Georgy Adelson-Velsky and Evgenii Landis, are a type of self-balancing binary search tree. In an AVL tree, the heights of the two child subtrees of any node differ by at most one. If at any time they differ by more than one, rebalancing is done to restore this property.

## Key Concepts
- **Balance Factor**: The difference between the heights of the left subtree and the right subtree for any node.
- **Rotations**: AVL trees may rotate in one of the following four ways to keep itself balanced:
    - **Left Rotation**: When a node is added into the right subtree of the right subtree, if the tree gets out of balance, we do a single left rotation.
    - **Right Rotation**: If a node is added to the left subtree of the left subtree, the AVL tree may get out of balance, we do a single right rotation.
    - **Left-Right Rotation**: A left-right rotation is a combination in which first left rotation takes place after that right rotation executes.
    - **Right-Left Rotation**: A right-left rotation is a combination in which first right rotation takes place after that left rotation executes.

## Operations
- **Insertion**: Adds a new node to the AVL tree. If the tree becomes unbalanced after insertion, it is rebalanced using rotation operations.
- **Deletion**: Removes a node from the AVL tree. If the tree becomes unbalanced after deletion, it is rebalanced using rotation operations.
- **Searching**: Finds a node in the AVL tree.
- **Traversal**: Visits each node in the AVL tree.

## Time Complexities
- **Insertion**: O(log n) in the best, average, and worst cases.
- **Deletion**: O(log n) in the best, average, and worst cases.
- **Searching**: O(log n) in the average and worst cases, and O(1) in the best case.
- **Traversal**: O(log n) in the best, average, and worst cases.

## Use Cases
- **Database Systems**: AVL trees are commonly used in database systems to index and search data. Their self-balancing property ensures efficient data retrieval operations, making them ideal for managing large datasets.
- **Auto-Completion and Spell Checking**: Autocomplete features in text editors and search engines heavily rely on AVL trees for quick searching and suggestions.
- **Network Routing**: In computer networks, routing tables often employ AVL trees to efficiently find the best route for data packets.
## Example
Let's consider an example with numbers:
# Left Rotation in AVL Trees
Let's say we have an AVL tree with the root node as 20, and it has two children: 10 on the left and 30 on the right. Now, we want to insert a new node with the value of 40. The new node would go to the right of node 30, making the tree unbalanced. Here's how the tree looks before the rotation:
```
  20
 /  \
10  30
      \
      40
```
Now, we perform a left rotation on the root node (20). Here's how it works:

1. `new_root = root_node.right_child:` The right child of the root node (30) becomes the new root.
2. `root_node.right_child = new_root.left_child:` The right child of the original root node (20) is now the left child of the new root (30), which is None in this case.
3. `new_root.left_child = root_node:` The original root node (20) becomes the left child of the new root (30).

After the rotation, the tree looks like this:
```
   30
  /  \
20   40
/
10
```
# Right Rotation in AVL Trees

Right rotation is one of the operations that AVL trees use to maintain their balance. It's used when the left subtree of a node is "heavier" (i.e., has a greater height) than the right subtree.

## Key Concepts
- **Right Rotation**: When a node is added into the left subtree of the left subtree, if the tree gets out of balance, we do a single right rotation.

## Example
Let's consider an example with numbers:

Let's say we have an AVL tree with the root node as 30, and it has two children: 20 on the left and 40 on the right. Now, we want to insert a new node with the value of 10. The new node would go to the left of node 20, making the tree unbalanced. Here's how the tree looks before the rotation:
```
  30
 /  \
20   40
/
10
```
Now, we perform a right rotation on the root node (30). Here's how it works:

1. `new_root = root_node.left_child:` The left child of the root node (20) becomes the new root.
2. `root_node.left_child = new_root.right_child:` The left child of the original root node (30) is now the right child of the new root (20), which is None in this case.
3. `new_root.right_child = root_node:` The original root node (30) becomes the right child of the new root (20).

After the rotation, the tree looks like this:

```
  20
 /  \
10  30
      \
      40
```
```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def left_rotate(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def right_rotate(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root 
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print("{0} ".format(root.key), end="")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print("{0} ".format(root.key), end="")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print("{0} ".format(root.key), end="")
```
# Red-Black Trees

Red-Black Trees are a type of self-balancing binary search tree, where each node contains an extra bit for denoting the color of the node, either red or black. A Red-Black Tree satisfies the following properties:

## Key Concepts
- **Node Colors**: Every node is either red or black.
- **Root Property**: The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
- **Leaf Property**: Every leaf (NIL) is black.
- **Red Node Property**: If a node is red, then both its children are black.
- **Depth Property**: For each node, any simple path from this node to any of its descendant leaves has the same black depth (the number of black nodes).

## Operations
- **Insertion**: Adds a new node to the Red-Black Tree. If the tree becomes unbalanced after insertion, it is rebalanced using rotation and color-flipping operations.
- **Deletion**: Removes a node from the Red-Black Tree. If the tree becomes unbalanced after deletion, it is rebalanced using rotation and color-flipping operations.
- **Searching**: Finds a node in the Red-Black Tree.
- **Traversal**: Visits each node in the Red-Black Tree.

## Time Complexities
- **Insertion**: O(log n) in the best, average, and worst cases.
- **Deletion**: O(log n) in the best, average, and worst cases.
- **Searching**: O(log n) in the average and worst cases, and O(1) in the best case.
- **Traversal**: O(n) in the best, average, and worst cases.

## Use Cases
- **Order Statistic Trees**: Red-Black Trees are used in the implementation of order-statistic trees which provides operations for finding the rank of a number, finding a number of a given rank, etc.
- **CPU Scheduling**: Linux uses Red-Black Trees in the Completely Fair Scheduler (CFS) for CPU scheduling.
- **Memory Management**: They are used in the memory management of several operating systems, including Linux and Windows.
```python
class Node:
    def __init__(self, data, color='red'):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color="black")
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
        self.root.color = "black"

    def left_rotate(self, node):
        pivot_node = node.right
        node.right = pivot_node.left
        if pivot_node.left != self.NIL:
            pivot_node.left.parent = node
        pivot_node.parent = node.parent
        if node.parent is None:
            self.root = pivot_node
        elif node == node.parent.left:
            node.parent.left = pivot_node
        else:
            node.parent.right = pivot_node
        pivot_node.left = node
        node.parent = pivot_node

    def right_rotate(self, node):
        pivot_node = node.left
        node.left = pivot_node.right
        if pivot_node.right != self.NIL:
            pivot_node.right.parent = node
        pivot_node.parent = node.parent
        if node.parent is None:
            self.root = pivot_node
        elif node == node.parent.right:
            node.parent.right = pivot_node
        else:
            node.parent.left = pivot_node
        pivot_node.right = node
        node.parent = pivot_node

    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node != self.NIL:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        return result
```
# Tries

Tries are a type of tree data structure used to efficiently store and retrieve strings (sequences of characters). Unlike binary search trees, tries don't store entire strings in each node. Instead, they utilize prefixes of strings for efficient searching and operations.

## Key Concepts

- **Nodes**: Each node in a Trie represents a single character in a string prefix.
- **Root**: The root node represents the empty string ('').
- **Edges**: Edges connect nodes, representing the progression of characters in a string.

## Operations

- **Insertion**: Inserts a new string into the Trie. Each character in the string is traversed, creating new nodes if necessary.
- **Search**: Searches for a specific string in the Trie. The search follows the character path in the Trie, checking for each character's presence.
- **Prefix Search**: Finds all strings starting with a given prefix. This efficiently retrieves all strings with a common beginning.
- **Deletion**: Removes a string from the Trie. If the string deletion leaves a node with no outgoing edges, it's potentially removed.

## Time Complexities

- **Insertion**: O(h), where h is the length of the string (average and worst case).
- **Search**: O(h), where h is the length of the string (average and worst case). O(1) if the search encounters a dead end early.
- **Prefix Search**: O(p), where p is the length of the prefix (average and worst case).
- **Deletion**: O(h), where h is the length of the string (average and worst case).

## Use Cases

- **Autocomplete**: Tries are a popular choice for implementing autocomplete features, suggesting words based on the user's typed prefix.
- **Spell Checkers**: Tries can be used to efficiently check for misspelled words by comparing them against a Trie containing correctly spelled words.
- **Network Routing**: IP addresses can be represented as Tries for efficient routing decisions in network protocols.
```python
class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Tries:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        if not self.root or not word:
            raise ValueError("Trie is empty or word is not provided")
        return self.delete_helper(self.root, word, 0)

    def delete_helper(self, node, word, index):
        if index == len(word):
            if not node.is_end:
                return False
            node.is_end = False
            return len(node.children) == 0

        char = word[index]
        if char not in node.children:
            return False

        if self.delete_helper(node.children[char], word, index + 1):
            del node.children[char]
            return len(node.children) == 0

        return False
```
# Segment Trees

Segment Trees are a data structure used for storing information about segments or intervals and allows for efficient querying and updating of these segments.

## Segments

The segments in a Segment Tree represent a range of elements in an array. Each node in the tree represents a segment of the array. The root of the tree represents the entire array, and each of its children represents a half of the array. This division continues recursively until each segment represents a single element.

## Structure of Segment Tree

A Segment Tree is a data structure that is built in a specific way:

1. **Recursive Construction**: A segment tree is built recursively, dividing the original array into segments until each segment represents a single element.

2. **Node Representation**: Each node in the tree represents an interval in the original array.

3. **Root Node**: The root node represents the entire array.

4. **Leaf Nodes**: Leaf nodes represent single elements in the array.

5. **Internal Nodes**: Internal nodes represent the union of the intervals of their children.

## Operations

Segment Trees support two main types of operations:

1. **Query**: This operation is used to compute some function over a range of elements. The function could be finding the sum, minimum, maximum, etc. The time complexity for this operation is **O(log n)**.

2. **Update**: This operation is used to update an element in the array. The time complexity for this operation is also **O(log n)**.

## Time Complexity

The time complexity of building a Segment Tree is **O(n)**. This is because we visit every node exactly once during the build process.

The time complexity of both query and update operations in a Segment Tree is **O(log n)**. This is because we traverse from the root of the tree to a leaf node, and the height of the tree is log(n).

## Applications

1. **Interval scheduling**: Segment trees can be used to efficiently schedule non-overlapping intervals, such as scheduling appointments or allocating resources.

2. **Range-based statistics**: Segment trees can be used to compute range-based statistics such as variance, standard deviation, and percentiles.

3. **Image processing**: Segment trees are used in image processing algorithms to divide an image into segments based on color, texture, or other attributes.
```
Array: 1 3 5 7 9 11

            36
           /  \
         9      27
        / \    /  \
       1   8  12  15
          / \  / \  / \
         1  3 5  7 9  11
```
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = self.build_tree(arr, 0, len(arr) - 1)

    def build_tree(self, arr, start, end):
        if start > end:
            return None
        if start == end:
            return Node(arr[start])

        mid = (start + end) // 2
        left_child = self.build_tree(arr, start, mid)
        right_child = self.build_tree(arr, mid + 1, end)

        node = Node(0)
        if left_child:
            node.data = node.data + left_child.data
            node.left = left_child
        if right_child:
            node.data = node.data + right_child.data
            node.right = right_child

        return node

    def query(self, root, query_start, query_end, start, end):
        if not root:
            return 0
        if start > query_end or end < query_start:
            return 0

        if start >= query_start and end <= query_end:
            return root.data

        mid = (start + end) // 2
        left_sum = self.query(root.left, query_start, query_end, start, mid)
        right_sum = self.query(root.right ,query_start, query_end, mid + 1, end)

        return left_sum + right_sum

    def update(self, root, index, value, start, end):
        if start == end:
            self.arr[index] = value
            root.data = value
        else:
            mid = (start + end) // 2
            if start <= index <= mid:
                self.update(root.left, index, value, start, mid)
            else:
                self.update(root.right, index, value, mid + 1, end)

        root.data = 0
        if root.left:
            root.data = root.data + root.left.data
        if root.right:
            root.data = root.data + root.right.data
```
# Fenwick Trees (Binary Indexed Trees)

Fenwick Trees or Binary Indexed Trees are a data structure used for storing information about an array of numbers, allowing prefix sums to be calculated efficiently.

## Basic Idea

The basic idea of a Fenwick Tree is that each integer can be represented as a sum of powers of two. Similarly, for a given array of size N, we can maintain an array BIT [] such that, at any index we can store the sum of some numbers of the given array.

## Operations

Fenwick Trees support two main types of operations:

1. **Point Update**: This operation is used to change the value stored at an index i. This operation takes **O(log n)** time.

2. **Range Sum Query**: This operation is used to find the sum of a prefix of length k. This operation also takes **O(log n)** time.

## Time Complexity

The time complexity of both point update and range sum query operations in a Fenwick Tree is **O(log n)**. This is because we traverse from the root of the tree to a leaf node, and the height of the tree is log(n).

# Applications

1. **Cumulative frequency tables**: Fenwick Trees can be used to efficiently compute cumulative frequency tables, which are useful in statistics and data analysis.

2. **Range sum queries**: Fenwick Trees can be used to efficiently compute the sum of a range of elements in an array.

3. **Point updates**: Fenwick Trees can be used to efficiently update the value of an element in an array.
```
Array: 1 3 5 7 9 11 13 15
Index: 1 2 3 4 5 6 7  8
Array: 1 4 5 16 9 20 13 64
``
```python
class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += (index & -index)

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= (index & -index)
        return sum
```
# Backtracking

Backtracking is an algorithm for finding solutions to computational problems, especially constraint satisfaction problems. It builds candidates for solutions and abandons a candidate if it cannot be extended to a valid solution.

## N-Queens Problem

The N-Queens problem is a classic problem in computer science. The goal is to place N queens on an NxN chessboard such that no two queens threaten each other.

## Backtracking Solution

The problem can be solved using backtracking. Queens are placed one by one in different columns. If we find a position in the current column where there is no clash with already placed queens, we mark this cell and move to the next column.

## Time Complexity

The time complexity of this algorithm is O(N!). In the first column, we have N choices to place the queen, in the second column at most N-1 choices, and so on. So, the total number of possibilities to check is N*(N-1)(N-2)…*1 = N!.

## Space Complexity

The space complexity of this algorithm is O(N^2). This is because we need a 2D array of size NxN to store the board configuration.

## Use Cases

The N-Queens problem has several real-world applications, including:

- Parallel computing: Used to benchmark parallel algorithms and architectures.
- Traffic control: Used in traffic signal control systems to reduce congestion and improve traffic flow.
- Database transactions: Used in database systems to test database transactions and concurrency control mechanisms.
```python
class NQueen:
    def safe(self, board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(self, board, col):
        if col >= len(board):
            return True

        for i in range(len(board)):
            if self.safe(board, i, col):
                board[i][col] = 1
                if self.solve(board, col + 1):
                    return True
                board[i][col] = 0  # Backtrack

        return False
```
# Greedy Algorithms

Greedy algorithms are a type of algorithm that makes the best choice at each step as it attempts to find the overall optimal solution.

## Key Points

- **Principle**: Greedy algorithms make the locally optimal choice at each step with the hope of finding a globally optimal solution.
- **Applications**: Used in various optimization problems like activity scheduling, knapsack problem, Huffman coding, minimum spanning tree, and shortest path problems.
- **Advantages**: They are simple and efficient.
- **Disadvantages**: They don't always guarantee the best solution as they make decisions based on current information without considering the impact on the overall solution.

## Activity Selection Problem

The activity selection problem is a classic example of a problem that can be solved using a greedy algorithm.

### Problem Statement

Given a list of activities with their start and end times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

### Greedy Approach

1. **Sort** the activities according to their finishing times.
2. **Start** with an empty schedule.
3. **Iterate** through the activities:
    - If the current activity's start time is greater than or equal to the finish time of the previously selected activity, add the current activity to the schedule.

This approach is greedy because it always selects the activity that finishes the earliest, allowing more activities to potentially fit in later.
```python
def select_activities(start, finish):
    n = len(start)
    activities = []
    
    i = 0
    activities.append(i)
    
    for j in range(1, n):
        if start[j] >= finish[i]:
            activities.append(j)
            i = j
    
    return activities
```
## Divide and Conquer: Conquer by Divide and Rule

Divide and conquer is a powerful algorithmic paradigm for solving complex problems by breaking them down into smaller, independent subproblems. This approach is particularly effective for problems that can be naturally divided into independent subproblems.

**Steps:**

1. **Divide:** Break the original problem into **smaller, independent subproblems** that resemble the original problem but are simpler to solve.
2. **Conquer:** Solve the subproblems **recursively**. If a subproblem is still too big, further divide it.
3. **Combine:** Merge the solutions of the subproblems to get the solution for the original problem.

**Benefits:**

* **Efficiency:** Dividing the problem often leads to faster algorithms compared to tackling it as a whole.
* **Parallelization:** In some cases, subproblems can be solved independently, making them suitable for parallel processing on multi-core systems.

## Merge Sort: Sorting by Divide and Conquer

Merge sort excels at sorting using the divide-and-conquer approach:

1. **Divide:** Split the input list into two (roughly) equal halves.
2. **Conquer:** Sort each half **recursively** using merge sort itself.
3. **Combine:** Merge the two sorted halves into a single sorted list. This involves comparing elements from both halves and placing the smaller element in the resulting sorted list.

**Properties:**

* **Time Complexity:** O(n log n) (average and worst case), making it efficient for large datasets.
* **Space Complexity:** O(n) due to the extra space needed for merging.
* **Stability:** It preserves the original order of equal elements.

## Quick Sort: Sorting with a Pivot

Quick sort is another efficient divide-and-conquer sorting algorithm:

1. **Divide:**
    * Choose a pivot element (often the first or last element).
    * Partition the list around the pivot: elements less than the pivot and elements greater than the pivot.
2. **Conquer:** Sort the two sub-arrays **recursively** using quick sort.
3. **Combine:** The sorted sub-arrays are already in their correct positions relative to each other since they were placed based on the pivot value.

**Properties:**

* **Average Time Complexity:** O(n log n), making it efficient for large datasets on average.
* **Worst Time Complexity:** O(n^2) in the case of a poorly chosen pivot (e.g., always the first or last element in a sorted or reverse-sorted array). In practice, this is uncommon with good pivot selection strategies.
* **Space Complexity:** O(log n) due to the recursive calls (typically lower than merge sort's space complexity).
* **Not Stable:** It may not preserve the original order of equal elements.

**In essence, both Merge Sort and Quick Sort leverage divide and conquer to achieve efficient sorting. Merge Sort prioritizes stability and space efficiency, while Quick Sort offers potentially faster average-case performance.**

## Dynamic Programming

### What is Dynamic Programming (DP)?

- **Definition:** Dynamic Programming solves complex problems by breaking them into simpler subproblems.
  
- **When to use:** If the problem exhibits Optimal Substructure and Overlapping Subproblems.

### Techniques

1. **Memoization:** Top-down approach that stores solutions of subproblems.
    
2. **Tabulation:** Bottom-up approach that solves all subproblems first.

### Advantages

- Efficiently solves complex problems.
    
- Avoids redundant calculations.

### Disadvantages

- Requires careful problem analysis.
    
- May require large memory for the table.

### Complexity

- **Time:** Depends on the number of subproblems and time to solve each. Often O(n), where n is the size of the input.
    
- **Space:** Depends on the number of subproblems. Often O(n).

### Common Problems

- Fibonacci sequence
- Longest Common Subsequence (LCS)
- Knapsack problem
- Coin Change problem
- Traveling Salesman Problem (TSP)

# Graphs

A **Graph** is a non-linear data structure consisting of nodes (or vertices) and edges. The edges link the nodes together.

## Graph Representations

There are two common ways to represent a graph in Python:

1. **Adjacency Matrix**
2. **Adjacency List**

# Adjacency Matrix

An **adjacency matrix** is a square matrix used to represent a finite graph. The elements of the matrix indicate whether pairs of nodes are adjacent or not in the graph.

## Operations

- **Add Node**: Add a row and column initialized to 0.
- **Add Edge**: Set the value of the cell at the intersection of the row of the first node and the column of the second node (and vice versa if the graph is undirected) to 1.
- **Remove Edge**: Similar to adding an edge, but set the value to 0.
- **Remove Node**: Remove the row and column corresponding to the node.

## Use Cases

Adjacency matrices are used when we need to quickly check if there is an edge connecting two nodes.

## Time and Space Complexity

- **Space Complexity**: The space complexity for an adjacency matrix representation is $$O(N^2)$$, where N is the number of nodes. This is because we need to store all possible edges between all pairs of nodes.
- **Time Complexity**: The time complexity to check if an edge exists between two nodes is $$O(1)$$, as it requires a single operation to check the value in the matrix. However, adding or removing a node is $$O(N^2)$$ because we may need to create a new matrix.
```python
class AdjacencyMatrix:
    def __init__(self):
        self.matrix = []

    def add_node(self):
        n = len(self.matrix)
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * (n + 1))

    def add_edge(self, i, j):
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1

    def remove_node(self, i):
        self.matrix.pop(i)
        for row in self.matrix:
            row.pop(i)

    def remove_edge(self, i, j):
        self.matrix[i][j] = 0
        self.matrix[j][i] = 0

    def disaplay(self):
        for row in self.matrix:
            print(row)
```

# Adjacency List

An **adjacency list** represents a graph as a map from nodes to lists of edges. 

## Operations

- **Add Node**: Add a key to the map with an empty list.
- **Add Edge**: Append the second node to the list of the first node.
- **Remove Edge**: Remove the second node from the list of the first node.
- **Remove Node**: Remove the key-value pair from the map.

## Use Cases

Adjacency lists are used for iterating over neighbors of a node or for sparse graphs.

## Time and Space Complexity

- **Space Complexity**: $$O(N + E)$$, where N is nodes and E is edges.
- **Time Complexity**: Checking an edge is $$O(N)$$. Adding a node or an edge is $$O(1)$$. Removing a node is $$O(N)$$. Removing an edge is $$O(E)$$.

# Breadth-First Search (BFS)

BFS is a graph traversal algorithm that explores all the vertices of a graph in breadth-first order, i.e., it explores all the vertices at the present “depth” before going to the next depth level.

## Operations

1. **Initialization**: Start by picking any node in the graph, marking it as visited and enqueue it into a queue.
2. **Exploration**: While the queue is not empty, dequeue a node from the queue, visit it, and enqueue all its unvisited neighbors.
3. **Termination**: The algorithm ends when the queue is empty.

## Use Cases

BFS is used in a wide range of applications, including:

1. **Shortest Path**: In an unweighted graph, BFS can find the shortest path between two nodes.
2. **Web Crawling**: Search engines use BFS to crawl pages on the web.
3. **Network Broadcasting**: BFS is used in broadcasting in a network, i.e., passing information to all nodes of a network.
4. **In AI/ML**: BFS is used in numerous algorithms in machine learning and AI, such as the A* search algorithm for pathfinding and graph traversals.

## Time and Space Complexity

* **Time Complexity**: The time complexity of BFS is O(V+E), where V is the number of vertices and E is the number of edges in the graph. This is because every vertex and every edge will be explored in the worst case.
* **Space Complexity**: The space complexity of BFS is O(V), where V is the maximum number of vertices on fringe of BFS. This is due to the storage needed for the queue.
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        current_node = queue.popleft()
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return visited
```

# Depth-First Search (DFS)

DFS is a graph traversal algorithm that explores all the vertices of a graph in depth-first order, i.e., it explores as far as possible along each branch before backtracking.

## Operations

1. **Initialization**: Start by picking any node in the graph, marking it as visited and pushing it into a stack.
2. **Exploration**: While the stack is not empty, peek at the top of the stack. If the top node has any unvisited neighbors, mark the neighbor as visited and push it into the stack. If it doesn’t have any unvisited neighbors, pop it from the stack.
3. **Termination**: The algorithm ends when the stack is empty.

## Use Cases

DFS is used in a wide range of applications, including:

- **Path Finding**: DFS can be used to find a path between two nodes in a graph.
- **Topological Sorting**: DFS is used in topological sorting, which is ordering of the nodes in a directed acyclic graph (DAG) where for every directed edge from node A to node B, A comes before B in the ordering.
- **Detecting Cycle**: DFS can be used to detect a cycle in a Graph. DFS on a tree does not encounter a cycle.

## Time and Space Complexity

- **Time Complexity**: The time complexity of DFS is $$O(V+E)$$, where $$V$$ is the number of vertices and $$E$$ is the number of edges in the graph. This is because every vertex and every edge will be explored in the worst case.
- **Space Complexity**: The space complexity of DFS is $$O(V)$$, where $$V$$ is the number of vertices. This is due to the usage of a stack data structure. This can also be seen as the maximum depth of the recursion tree (in case of recursive implementation).

```python
def dfs(graph, start, visited=None):

    if not visited:
        visited =  set()
    visited.add(start)

    for next_node in (graph[start] - visited):
        dfs(graph, next_node, visited)

    return visited
```
# Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest paths between nodes in a graph. It was created by Edsger W. Dijkstra in 1956.

## Operations
- Initialization: Set the source node distance to 0, others to infinity. Mark all nodes unvisited.
- Selection: Choose the unvisited node with the smallest distance.
- Update: Calculate tentative distances to neighbors and update if smaller.
- Mark as Visited: Mark the current node as visited.
- Repeat: Continue until all nodes are visited or the smallest distance is infinity.

## Use Cases
- GPS navigation
- Network routing
- Geographic information systems (GIS)
- Game development
- Robotic navigation

## Complexity
### Time Complexity:
- Simple array: O(V^2)
- Priority queue (binary heap): O((V + E) log V)
- Fibonacci heap: O(E + V log V)

### Space Complexity: O(V + E)
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances
```

# Bellman-Ford Algorithm

Bellman-Ford algorithm computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.

## Operations
- Initialization: Set the source node distance to 0, others to infinity.
- Relaxation: For the graph having N vertices, all the edges should be relaxed N-1 times.
- Negative Cycle Check: Relax all the edge one more time and if the shortest distance for any node reduces then we can say that a negative cycle exists.

## Use Cases
- GPS for computers
- Handling Negative Weights
- Detecting Negative Cycles

## Complexity
### Time Complexity:
- Bellman-Ford runs in time O(VE), where V and E are the number of vertices and edges respectively.

### Space Complexity: O(V + E)
```python
def bellman_ford(graph, source):
    distance = {vertex: float('infinity') for vertex in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbour, weight in graph[vertex].items():
                if distance[vertex] + weight < distance[neighbour]:
                    distance[neighbour] = distance[vertex] + weight

    for vertex in graph:
        for neighbour, weight in graph[vertex].items():
            if distance[vertex] + weight < distance[neighbour]:
                return "Negative weight cycle detected"

    return distance
```
# Floyd-Warshall Algorithm

The Floyd-Warshall algorithm is used to find shortest paths in a weighted graph with positive or negative edge weights (but no negative cycles).

## Operations

- **Initialization**: Create a matrix, where the cell [i][j] is filled with the weight of the edge from i to j. If there is no direct edge between i and j, the cell is filled with infinity.
- **Path Calculation**: For each pair of vertices (i, j), consider all other vertices (k). If the path from i to k to j is shorter than the direct path from i to j, update the cell [i][j] with the new distance.
- **Negative Cycle Check**: If the distance from a vertex to itself becomes negative, a negative cycle exists.

## Use Cases

- All-Pairs Shortest Path Problem
- Network Routing Protocols
- In Game Theory and Economics

## Complexity

- **Time Complexity**: The Floyd-Warshall algorithm runs in time $$O(V^3)$$, where V is the number of vertices.
- **Space Complexity**: $$O(V^2)$$
```python
def floyd_warshall(graph):
    n = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
```

# Ford-Fulkerson Algorithm: Maximum Flow in Networks

The Ford-Fulkerson algorithm is used to find the maximum flow from a source vertex s to a sink vertex t in a directed graph. It is a greedy algorithm that iteratively finds augmenting paths from s to t and increases the flow along these paths until no more augmenting paths exist.

## Use Cases:
- **Transportation networks**: Optimizing traffic flow on roads or data flow in a computer network.
- **Production planning**: Determining maximum production output considering machine capacities.

## Operations:
1. **Initialization**: Set all flows to zero.
2. **Augmenting Path**: Find a path from source to sink in the residual network (original network with used capacities subtracted).
3. **Flow Update**: If an augmenting path exists, update flow along the path by its minimum residual capacity. Repeat steps 2-3 until no augmenting path is found.

## Complexity:
- **Time**: $$O(E \times F)$$, where $$E$$ is edges and $$F$$ is the maximum flow value (worst-case can be slow in practice).
- **Space**: $$O(V)$$, where $$V$$ is vertices in the network.
```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.capacity = defaultdict(int)
        for u, v, cap in graph:
            self.capacity[u, v] = cap

    def bfs(self, source, sink, parent):
        visited = [False] * len(self.graph)
        queue = deque([source])
        visited[source] = True
        while queue:
            u = queue.popleft()
            for v in range(len(self.graph)):
                if not visited[v] and self.capacity[u, v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def edmonds_karp(self, source, sink):
        parent = [-1] * len(self.graph)
        max_flow = 0
        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            v = sink
            while v != source:
                path_flow = min(path_flow, self.capacity[parent[v], v])
                v = parent[v]
            max_flow += path_flow
            u = sink
            while u != source:
                v = parent[u]
                self.capacity[v, u] -= path_flow
                self.capacity[u, v] += path_flow
                u = v
        return max_flow
```

# Edmonds-Karp Algorithm: Faster Max Flow

The Edmonds-Karp algorithm is an implementation of the Ford-Fulkerson method that uses BFS to find augmenting paths, resulting in faster execution.

## Use Cases:
- **Transportation networks**: Optimizing traffic flow on roads or data flow in a computer network.
- **Production planning**: Determining maximum production output considering machine capacities.

## Operations:
1. **Initialization**: Set all flows to zero.
2. **Shortest Augmenting Path**: Find the shortest path from source to sink in the residual network (using Breadth-First Search).
3. **Flow Update**: If a shortest path exists, update flow along the path by its minimum residual capacity. Repeat steps 2-3 until no path is found.

## Complexity:
- **Time**: $$O(V \times E^2)$$, where $$V$$ is vertices and $$E$$ is edges (generally faster than Ford-Fulkerson in practice).
- **Space**: $$O(V)$$, where $$V$$ is vertices in the network.
```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.capacity = defaultdict(int)
        for u, v, cap in graph:
            self.capacity[u, v] = cap

    def bfs(self, source, sink, parent):
        visited = [False] * len(self.graph)
        queue = deque([source])
        visited[source] = True
        while queue:
            u = queue.popleft()
            for v in range(len(self.graph)):
                if not visited[v] and self.capacity[u, v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def edmonds_karp(self, source, sink):
        parent = [-1] * len(self.graph)
        max_flow = 0
        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            v = sink
            while v != source:
                path_flow = min(path_flow, self.capacity[parent[v], v])
                v = parent[v]
            max_flow += path_flow
            u = sink
            while u != source:
                v = parent[u]
                self.capacity[v, u] -= path_flow
                self.capacity[u, v] += path_flow
                u = v
        return max_flow
```

# Two-Pointer Technique

## Definition
The two-pointer technique is a method that uses two pointers which navigate through the array or list simultaneously based on certain conditions.

## Use Cases
1. **Finding a pair in an array with a given sum**: Two pointers start, one from the beginning of the array and the other from the end. They move towards each other until they either meet or find the required pair.
2. **Reverse a string or array**: One pointer starts at the beginning and the other at the end. They move towards each other, swapping elements until they meet or cross each other.
3. **Linked List Problems**: Detecting a cycle in a linked list, finding the middle of a linked list, or finding the nth node from the end of a linked list.
4. **Array Problems**: Removing duplicates from a sorted array, finding the maximum sum of a subarray of size 'k' (sliding window).

## Advantages
1. **Efficiency**: In many cases, the two-pointer technique can reduce the time complexity from $$O(n^2)$$ to $$O(n)$$.
2. **Simplicity**: The two-pointer technique often simplifies the code and makes it easier to understand.
```python
def removeDuplicates(nums):
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
```