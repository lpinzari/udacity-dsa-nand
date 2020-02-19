
## Problem statement

Given an array `arr` and a target element `target`, find the last index of occurence of `target` in `arr` using recursion. If `target` is not present in `arr`, return `-1`.

For example:

1. For `arr = [1, 2, 5, 5, 4]` and `target = 5`, `output = 3`

2. For `arr = [1, 2, 5, 5, 4]` and `target = 7`, `output = -1`


```python
def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """
    pass
```

<span class="graffiti-highlight graffiti-id_vwcsmcw-id_flmfhqn"><i></i><button>Hide Solution</button></span>


```python
# Solution
def last_index(arr, target):
    print('---- last_index({},{}) ---- START'.format(arr, target))
    # we start looking from the last index
    output = last_index_arr(arr, target, len(arr) - 1)
    print('---- last_index({},{}) ---- END'.format(arr, target))
    return output


def last_index_arr(arr, target, index):
    print('---- last_index_arr({},{},{}) ---- START'.format(arr, target, index))
    if index < 0:
        print('Base case: -1')
        return -1
    
    # check if target is found
    if arr[index] == target:
        print('Base case: {}'.format(arr[index]))
        return index

    # else make a recursive call to the rest of the array
    output = last_index_arr(arr, target, index - 1)
    print('---- last_index_arr({},{},{}) ---- END'.format(arr, target, index))
    return output
```


```python
def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print("False")
```


```python
arr = [1, 2, 5, 5, 4]
target = 5
solution = 3

test_case = [arr, target, solution]
test_function(test_case)
```

    ---- last_index([1, 2, 5, 5, 4],5) ---- START
    ---- last_index_arr([1, 2, 5, 5, 4],5,4) ---- START
    ---- last_index_arr([1, 2, 5, 5, 4],5,3) ---- START
    Base case: 5
    ---- last_index_arr([1, 2, 5, 5, 4],5,4) ---- END
    ---- last_index([1, 2, 5, 5, 4],5) ---- END
    Pass



```python
arr = [1, 2, 5, 5, 4]
target = 7
solution = -1

test_case = [arr, target, solution]
test_function(test_case)
```

    ---- last_index([1, 2, 5, 5, 4],7) ---- START
    ---- last_index_arr([1, 2, 5, 5, 4],7,4) ---- START
    ---- last_index_arr([1, 2, 5, 5, 4],7,3) ---- START
    ---- last_index_arr([1, 2, 5, 5, 4],7,2) ---- START
    ---- last_index_arr([1, 2, 5, 5, 4],7,1) ---- START
    ---- last_index_arr([1, 2, 5, 5, 4],7,0) ---- START
    ---- last_index_arr([1, 2, 5, 5, 4],7,-1) ---- START
    Base case: -1
    ---- last_index_arr([1, 2, 5, 5, 4],7,0) ---- END
    ---- last_index_arr([1, 2, 5, 5, 4],7,1) ---- END
    ---- last_index_arr([1, 2, 5, 5, 4],7,2) ---- END
    ---- last_index_arr([1, 2, 5, 5, 4],7,3) ---- END
    ---- last_index_arr([1, 2, 5, 5, 4],7,4) ---- END
    ---- last_index([1, 2, 5, 5, 4],7) ---- END
    Pass



```python
arr = [91, 19, 3, 8, 9]
target = 91
solution = 0

test_case = [arr, target, solution]
test_function(test_case)
```

    ---- last_index([91, 19, 3, 8, 9],91) ---- START
    ---- last_index_arr([91, 19, 3, 8, 9],91,4) ---- START
    ---- last_index_arr([91, 19, 3, 8, 9],91,3) ---- START
    ---- last_index_arr([91, 19, 3, 8, 9],91,2) ---- START
    ---- last_index_arr([91, 19, 3, 8, 9],91,1) ---- START
    ---- last_index_arr([91, 19, 3, 8, 9],91,0) ---- START
    Base case: 91
    ---- last_index_arr([91, 19, 3, 8, 9],91,1) ---- END
    ---- last_index_arr([91, 19, 3, 8, 9],91,2) ---- END
    ---- last_index_arr([91, 19, 3, 8, 9],91,3) ---- END
    ---- last_index_arr([91, 19, 3, 8, 9],91,4) ---- END
    ---- last_index([91, 19, 3, 8, 9],91) ---- END
    Pass



```python
arr = [1, 1, 1, 1, 1, 1]
target = 1
solution = 5

test_case = [arr, target, solution]
test_function(test_case)
```

    ---- last_index([1, 1, 1, 1, 1, 1],1) ---- START
    ---- last_index_arr([1, 1, 1, 1, 1, 1],1,5) ---- START
    Base case: 1
    ---- last_index([1, 1, 1, 1, 1, 1],1) ---- END
    Pass



```python

```
