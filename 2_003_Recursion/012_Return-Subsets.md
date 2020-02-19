
### Problem Statement


Given an integer array, find and return all the subsets of the array.
The order of subsets in the output array is not important. However the order of elements in a particular subset should remain the same as in the input array.

*Note: An empty set will be represented by an empty list*

**Example 1**

```
arr = [9]

output = [[]
          [9]]
```

**Example 2**

```
arr = [9, 12, 15]

output =  [[],
           [15],
           [12],
           [12, 15],
           [9],
           [9, 15],
           [9, 12],
           [9, 12, 15]]
```


```python
def subsets(arr):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    TODO: complete this method to return subsets of an array
    """
    pass
```

<span class="graffiti-highlight graffiti-id_u30cq9y-id_2p8ft48"><i></i><button>Hide Solution</button></span>


```python
# Solution
def subsets(arr):
    print('---- subsets({}) ---- START'.format(arr))
    output = return_subsets(arr, 0)
    print('---- subsets({}) ---- END'.format(arr))
    return output

def return_subsets(arr, index):
    print('---- return_subsets({},{}) ---- START'.format(arr, index))
    if index >= len(arr):
        print('Base case: [[]]')
        return [[]]

    small_output = return_subsets(arr, index + 1)
    print('---- return_subsets({},{}) ---- CALL'.format(arr, index))
    print('small_output: {}'.format(small_output))

    output = list()
    # append existing subsets
    print('for loop: small_output')
    for element in small_output:
        print('\t element: {}'.format(element))
        output.append(element)
    
    print('output: {}'.format(output))
    # add current elements to existing subsets and add them to the output
    print('for loop: small_output')
    counter = 0
    for element in small_output:
        print('iteration: {}'.format(counter))
        print('\t arr[{}]: {}'.format(index,arr[index]))
        print('\t element: {}'.format(element))
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
        print('\t current: {}'.format(current))
        print('\t output: {}'.format(output))
        counter += 1
    
    print('output: {}'.format(output))
    print('---- return_subsets({},{}) ---- END'.format(arr, index))
    return output
```


```python
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = subsets(arr)
        
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")    
```


```python
arr = [9]
solution = [[], [9]]

test_case = [arr, solution]
test_function(test_case)
```

    ---- subsets([9]) ---- START
    ---- return_subsets([9],0) ---- START
    ---- return_subsets([9],1) ---- START
    Base case: [[]]
    ---- return_subsets([9],0) ---- CALL
    small_output: [[]]
    for loop: small_output
    	 element: []
    output: [[]]
    for loop: small_output
    iteration: 0
    	 arr[0]: 9
    	 element: []
    	 current: [9]
    	 output: [[], [9]]
    output: [[], [9]]
    ---- return_subsets([9],0) ---- END
    ---- subsets([9]) ---- END
    Pass



```python
arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
test_case = [arr, solution]
test_function(test_case)
```

    ---- subsets([5, 7]) ---- START
    ---- return_subsets([5, 7],0) ---- START
    ---- return_subsets([5, 7],1) ---- START
    ---- return_subsets([5, 7],2) ---- START
    Base case: [[]]
    ---- return_subsets([5, 7],1) ---- CALL
    small_output: [[]]
    for loop: small_output
    	 element: []
    output: [[]]
    for loop: small_output
    iteration: 0
    	 arr[1]: 7
    	 element: []
    	 current: [7]
    	 output: [[], [7]]
    output: [[], [7]]
    ---- return_subsets([5, 7],1) ---- END
    ---- return_subsets([5, 7],0) ---- CALL
    small_output: [[], [7]]
    for loop: small_output
    	 element: []
    	 element: [7]
    output: [[], [7]]
    for loop: small_output
    iteration: 0
    	 arr[0]: 5
    	 element: []
    	 current: [5]
    	 output: [[], [7], [5]]
    iteration: 1
    	 arr[0]: 5
    	 element: [7]
    	 current: [5, 7]
    	 output: [[], [7], [5], [5, 7]]
    output: [[], [7], [5], [5, 7]]
    ---- return_subsets([5, 7],0) ---- END
    ---- subsets([5, 7]) ---- END
    Pass



```python
arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]

test_case = [arr, solution]
test_function(test_case)
```

    ---- subsets([9, 12, 15]) ---- START
    ---- return_subsets([9, 12, 15],0) ---- START
    ---- return_subsets([9, 12, 15],1) ---- START
    ---- return_subsets([9, 12, 15],2) ---- START
    ---- return_subsets([9, 12, 15],3) ---- START
    Base case: [[]]
    ---- return_subsets([9, 12, 15],2) ---- CALL
    small_output: [[]]
    for loop: small_output
    	 element: []
    output: [[]]
    for loop: small_output
    iteration: 0
    	 arr[2]: 15
    	 element: []
    	 current: [15]
    	 output: [[], [15]]
    output: [[], [15]]
    ---- return_subsets([9, 12, 15],2) ---- END
    ---- return_subsets([9, 12, 15],1) ---- CALL
    small_output: [[], [15]]
    for loop: small_output
    	 element: []
    	 element: [15]
    output: [[], [15]]
    for loop: small_output
    iteration: 0
    	 arr[1]: 12
    	 element: []
    	 current: [12]
    	 output: [[], [15], [12]]
    iteration: 1
    	 arr[1]: 12
    	 element: [15]
    	 current: [12, 15]
    	 output: [[], [15], [12], [12, 15]]
    output: [[], [15], [12], [12, 15]]
    ---- return_subsets([9, 12, 15],1) ---- END
    ---- return_subsets([9, 12, 15],0) ---- CALL
    small_output: [[], [15], [12], [12, 15]]
    for loop: small_output
    	 element: []
    	 element: [15]
    	 element: [12]
    	 element: [12, 15]
    output: [[], [15], [12], [12, 15]]
    for loop: small_output
    iteration: 0
    	 arr[0]: 9
    	 element: []
    	 current: [9]
    	 output: [[], [15], [12], [12, 15], [9]]
    iteration: 1
    	 arr[0]: 9
    	 element: [15]
    	 current: [9, 15]
    	 output: [[], [15], [12], [12, 15], [9], [9, 15]]
    iteration: 2
    	 arr[0]: 9
    	 element: [12]
    	 current: [9, 12]
    	 output: [[], [15], [12], [12, 15], [9], [9, 15], [9, 12]]
    iteration: 3
    	 arr[0]: 9
    	 element: [12, 15]
    	 current: [9, 12, 15]
    	 output: [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]
    output: [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]
    ---- return_subsets([9, 12, 15],0) ---- END
    ---- subsets([9, 12, 15]) ---- END
    Pass



```python
arr = [9, 8, 9, 8]
solution = [[],
[8],
[9],
[9, 8],
[8],
[8, 8],
[8, 9],
[8, 9, 8],
[9],
[9, 8],
[9, 9],
[9, 9, 8],
[9, 8],
[9, 8, 8],
[9, 8, 9],
[9, 8, 9, 8]]

test_case = [arr, solution]
test_function(test_case)
```

    ---- subsets([9, 8, 9, 8]) ---- START
    ---- return_subsets([9, 8, 9, 8],0) ---- START
    ---- return_subsets([9, 8, 9, 8],1) ---- START
    ---- return_subsets([9, 8, 9, 8],2) ---- START
    ---- return_subsets([9, 8, 9, 8],3) ---- START
    ---- return_subsets([9, 8, 9, 8],4) ---- START
    Base case: [[]]
    ---- return_subsets([9, 8, 9, 8],3) ---- CALL
    small_output: [[]]
    for loop: small_output
    	 element: []
    output: [[]]
    for loop: small_output
    iteration: 0
    	 arr[3]: 8
    	 element: []
    	 current: [8]
    	 output: [[], [8]]
    output: [[], [8]]
    ---- return_subsets([9, 8, 9, 8],3) ---- END
    ---- return_subsets([9, 8, 9, 8],2) ---- CALL
    small_output: [[], [8]]
    for loop: small_output
    	 element: []
    	 element: [8]
    output: [[], [8]]
    for loop: small_output
    iteration: 0
    	 arr[2]: 9
    	 element: []
    	 current: [9]
    	 output: [[], [8], [9]]
    iteration: 1
    	 arr[2]: 9
    	 element: [8]
    	 current: [9, 8]
    	 output: [[], [8], [9], [9, 8]]
    output: [[], [8], [9], [9, 8]]
    ---- return_subsets([9, 8, 9, 8],2) ---- END
    ---- return_subsets([9, 8, 9, 8],1) ---- CALL
    small_output: [[], [8], [9], [9, 8]]
    for loop: small_output
    	 element: []
    	 element: [8]
    	 element: [9]
    	 element: [9, 8]
    output: [[], [8], [9], [9, 8]]
    for loop: small_output
    iteration: 0
    	 arr[1]: 8
    	 element: []
    	 current: [8]
    	 output: [[], [8], [9], [9, 8], [8]]
    iteration: 1
    	 arr[1]: 8
    	 element: [8]
    	 current: [8, 8]
    	 output: [[], [8], [9], [9, 8], [8], [8, 8]]
    iteration: 2
    	 arr[1]: 8
    	 element: [9]
    	 current: [8, 9]
    	 output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9]]
    iteration: 3
    	 arr[1]: 8
    	 element: [9, 8]
    	 current: [8, 9, 8]
    	 output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8]]
    output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8]]
    ---- return_subsets([9, 8, 9, 8],1) ---- END
    ---- return_subsets([9, 8, 9, 8],0) ---- CALL
    small_output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8]]
    for loop: small_output
    	 element: []
    	 element: [8]
    	 element: [9]
    	 element: [9, 8]
    	 element: [8]
    	 element: [8, 8]
    	 element: [8, 9]
    	 element: [8, 9, 8]
    output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8]]
    for loop: small_output
    iteration: 0
    	 arr[0]: 9
    	 element: []
    	 current: [9]
    	 output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8], [9]]
    iteration: 1
    	 arr[0]: 9
    	 element: [8]
    	 current: [9, 8]
    	 output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8], [9], [9, 8]]
    iteration: 2
    	 arr[0]: 9
    	 element: [9]
    	 current: [9, 9]
    	 output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8], [9], [9, 8], [9, 9]]
    iteration: 3
    	 arr[0]: 9
    	 element: [9, 8]
    	 current: [9, 9, 8]
    	 output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8], [9], [9, 8], [9, 9], [9, 9, 8]]
    iteration: 4
    	 arr[0]: 9
    	 element: [8]
    	 current: [9, 8]
    	 output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8], [9], [9, 8], [9, 9], [9, 9, 8], [9, 8]]
    iteration: 5
    	 arr[0]: 9
    	 element: [8, 8]
    	 current: [9, 8, 8]
    	 output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8], [9], [9, 8], [9, 9], [9, 9, 8], [9, 8], [9, 8, 8]]
    iteration: 6
    	 arr[0]: 9
    	 element: [8, 9]
    	 current: [9, 8, 9]
    	 output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8], [9], [9, 8], [9, 9], [9, 9, 8], [9, 8], [9, 8, 8], [9, 8, 9]]
    iteration: 7
    	 arr[0]: 9
    	 element: [8, 9, 8]
    	 current: [9, 8, 9, 8]
    	 output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8], [9], [9, 8], [9, 9], [9, 9, 8], [9, 8], [9, 8, 8], [9, 8, 9], [9, 8, 9, 8]]
    output: [[], [8], [9], [9, 8], [8], [8, 8], [8, 9], [8, 9, 8], [9], [9, 8], [9, 9], [9, 9, 8], [9, 8], [9, 8, 8], [9, 8, 9], [9, 8, 9, 8]]
    ---- return_subsets([9, 8, 9, 8],0) ---- END
    ---- subsets([9, 8, 9, 8]) ---- END
    Pass



```python

```
