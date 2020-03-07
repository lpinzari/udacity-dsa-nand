
# Heapsort

A heapsort is an in-place sorting algorithm that treats an array like a binary tree and moves the largest values to the end of the heap until the full array is sorted.  

The main steps in a heapsort are:
1. Convert the array into a maxheap (a complete binary tree with decreasing values) 
2. Swap the top element with the last element in the array (putting it in it's correct final position)
3. Repeat with `arr[:len(arr)-1]` (all but the sorted elements)

## Visualization of a heapsort
![animation of a heap sort](https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif)

["Heapsort example"](https://commons.wikimedia.org/wiki/File:Heapsort-example.gif) by Swfung8. Used under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en).

## Problem statement

In the cell below, see if you can code a `heapsort` function that takes an array (or Python list) and performs a heapsort on it. You will have to complete the heapify


```python
def heapsort(arr):
    heapify(arr, len(arr), 0)
    
def heapify():
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """
```

<span class="graffiti-highlight graffiti-id_1h50lwk-id_kuae7he"><i></i><button>Hide Solution</button></span>


```python
# Solution

def heapify(arr, n, i):
    # Using i as the index of the current node, find the 2 child nodes (if the array were a binary tree)
    # and find the largest value.   If one of the children is larger swap the values and recurse into that subree
    # Heapify-UP
    
    # consider current index as largest
    largest_index = i 
    left_node = 2 * i + 1     
    right_node = 2 * i + 2     
  
    # compare with left child (we compare first the indicies to check IndexOutOfBounds)
    if left_node < n and arr[i] < arr[left_node]: 
        largest_index = left_node
  
    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]: 
        largest_index = right_node
  
    # if either of left / right child is the largest node swapping the values largest up and lowest down
    # Call recursively the function.
    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i] 
        heapify(arr, n, largest_index) 
        
def heapsort(arr):
    # First convert the array into a maxheap by calling heapify on each node, starting from the end   
    # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.  Continue to do this until the whole
    # array is sorted
    n = len(arr) 
    
    print('array: {}'.format(arr))
    # Build a maxheap. Countdown i: len(arr)= n to 0 (we start from the end of the array) range(start,stop,step)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    
    print('heapify: {}'.format(arr))
  
    # One by one extract elements from the root (they are the maximum) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap the root value (maximum) with the i-th node
        heapify(arr, i, 0)
    print('array: {}'.format(arr))
```


```python
def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")
```


```python
arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]

test_case = [arr, solution]

test_function(test_case)

```

    array: [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
    heapify: [9, 8, 9, 7, 4, 5, 4, 3, 6, 1, 3, 0]
    array: [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
    Pass



```python
arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

```

    array: [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
    heapify: [5, 5, 5, 4, 4, 3, 4, 3, 4, 3]
    array: [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
    Pass



```python
arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)

```

    array: [99]
    heapify: [99]
    array: [99]
    Pass



```python
arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)

```

    array: [0, 1, 2, 5, 12, 21, 0]
    heapify: [21, 12, 2, 5, 1, 0, 0]
    array: [0, 0, 1, 2, 5, 12, 21]
    Pass



```python

```
