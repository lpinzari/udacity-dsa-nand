
## Problem Statement

Define a procedure, `deep_reverse`, that takes as input a list, and returns a new list that is the deep reverse of the input list.  
This means it reverses all the elements in the list, and if any of those elements are lists themselves, reverses all the elements in the inner list, all the way down. 

>Note: The procedure must not change the input list itself.





```python
def deep_reverse(arr):
    pass
```

<span class="graffiti-highlight graffiti-id_25r0ar8-id_l0hi76f"><i></i><button>Hide Solution</button></span>


```python
def is_list(element):
    """
    Check if element is a Python list
    """
    return isinstance(element, list)

def deep_reverse(arr):
    """
    Function to deep_reverse an input list
    """
    print('---- deep_reverse({}) ---- START '.format(arr))
    output = deep_reverse_func(arr,0)
    print('---- deep_reverse({}) ---- END'.format(arr))
    return output

def deep_reverse_func(arr, index):
    """
    Recursive function to deep_reverse the input list
    index: position in the array of the element to append
    """
    print('---- deep_reverse_func({},{}) ---- START'.format(arr, index))
    # Base Case
    if index == len(arr):
        print('Base case: {}'.format(list()))
        print('---- deep_reverse_func({},{}) ---- END'.format(arr, index))
        return list()
    
    output = deep_reverse_func(arr, index + 1)
    print('---- deep_reverse_func({},{}) ---- CALL'.format(arr, index))
    print('output: {}'.format(output))
    
    # if element is a list --> deep_reverse the list
    if is_list(arr[index]):
        print('The item in arr[{}]: {} is a list'.format(index,arr[index]))
        to_append = deep_reverse(arr[index])
    else:
        to_append = arr[index]
        
    output.append(to_append)
    print('to_append: {}'.format(to_append))
    print('output: {}'.format(output))
    print('---- deep_reverse_func({},{}) ---- END'.format(arr, index))
    return output
```


```python
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)

    if output == solution:
        print("Pass")
    else:
        print("False")
```


```python
arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)
```

    ---- deep_reverse([1, 2, 3, 4, 5]) ---- START 
    ---- deep_reverse_func([1, 2, 3, 4, 5],0) ---- START
    ---- deep_reverse_func([1, 2, 3, 4, 5],1) ---- START
    ---- deep_reverse_func([1, 2, 3, 4, 5],2) ---- START
    ---- deep_reverse_func([1, 2, 3, 4, 5],3) ---- START
    ---- deep_reverse_func([1, 2, 3, 4, 5],4) ---- START
    ---- deep_reverse_func([1, 2, 3, 4, 5],5) ---- START
    Base case: []
    ---- deep_reverse_func([1, 2, 3, 4, 5],5) ---- END
    ---- deep_reverse_func([1, 2, 3, 4, 5],4) ---- CALL
    output: []
    to_append: 5
    output: [5]
    ---- deep_reverse_func([1, 2, 3, 4, 5],4) ---- END
    ---- deep_reverse_func([1, 2, 3, 4, 5],3) ---- CALL
    output: [5]
    to_append: 4
    output: [5, 4]
    ---- deep_reverse_func([1, 2, 3, 4, 5],3) ---- END
    ---- deep_reverse_func([1, 2, 3, 4, 5],2) ---- CALL
    output: [5, 4]
    to_append: 3
    output: [5, 4, 3]
    ---- deep_reverse_func([1, 2, 3, 4, 5],2) ---- END
    ---- deep_reverse_func([1, 2, 3, 4, 5],1) ---- CALL
    output: [5, 4, 3]
    to_append: 2
    output: [5, 4, 3, 2]
    ---- deep_reverse_func([1, 2, 3, 4, 5],1) ---- END
    ---- deep_reverse_func([1, 2, 3, 4, 5],0) ---- CALL
    output: [5, 4, 3, 2]
    to_append: 1
    output: [5, 4, 3, 2, 1]
    ---- deep_reverse_func([1, 2, 3, 4, 5],0) ---- END
    ---- deep_reverse([1, 2, 3, 4, 5]) ---- END
    Pass



```python
arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)
```

    ---- deep_reverse([1, 2, [3, 4, 5], 4, 5]) ---- START 
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],0) ---- START
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],1) ---- START
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],2) ---- START
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],3) ---- START
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],4) ---- START
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],5) ---- START
    Base case: []
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],5) ---- END
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],4) ---- CALL
    output: []
    to_append: 5
    output: [5]
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],4) ---- END
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],3) ---- CALL
    output: [5]
    to_append: 4
    output: [5, 4]
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],3) ---- END
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],2) ---- CALL
    output: [5, 4]
    The item in arr[2]: [3, 4, 5] is a list
    ---- deep_reverse([3, 4, 5]) ---- START 
    ---- deep_reverse_func([3, 4, 5],0) ---- START
    ---- deep_reverse_func([3, 4, 5],1) ---- START
    ---- deep_reverse_func([3, 4, 5],2) ---- START
    ---- deep_reverse_func([3, 4, 5],3) ---- START
    Base case: []
    ---- deep_reverse_func([3, 4, 5],3) ---- END
    ---- deep_reverse_func([3, 4, 5],2) ---- CALL
    output: []
    to_append: 5
    output: [5]
    ---- deep_reverse_func([3, 4, 5],2) ---- END
    ---- deep_reverse_func([3, 4, 5],1) ---- CALL
    output: [5]
    to_append: 4
    output: [5, 4]
    ---- deep_reverse_func([3, 4, 5],1) ---- END
    ---- deep_reverse_func([3, 4, 5],0) ---- CALL
    output: [5, 4]
    to_append: 3
    output: [5, 4, 3]
    ---- deep_reverse_func([3, 4, 5],0) ---- END
    ---- deep_reverse([3, 4, 5]) ---- END
    to_append: [5, 4, 3]
    output: [5, 4, [5, 4, 3]]
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],2) ---- END
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],1) ---- CALL
    output: [5, 4, [5, 4, 3]]
    to_append: 2
    output: [5, 4, [5, 4, 3], 2]
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],1) ---- END
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],0) ---- CALL
    output: [5, 4, [5, 4, 3], 2]
    to_append: 1
    output: [5, 4, [5, 4, 3], 2, 1]
    ---- deep_reverse_func([1, 2, [3, 4, 5], 4, 5],0) ---- END
    ---- deep_reverse([1, 2, [3, 4, 5], 4, 5]) ---- END
    Pass



```python
arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)
```

    ---- deep_reverse([1, [2, 3, [4, [5, 6]]]]) ---- START 
    ---- deep_reverse_func([1, [2, 3, [4, [5, 6]]]],0) ---- START
    ---- deep_reverse_func([1, [2, 3, [4, [5, 6]]]],1) ---- START
    ---- deep_reverse_func([1, [2, 3, [4, [5, 6]]]],2) ---- START
    Base case: []
    ---- deep_reverse_func([1, [2, 3, [4, [5, 6]]]],2) ---- END
    ---- deep_reverse_func([1, [2, 3, [4, [5, 6]]]],1) ---- CALL
    output: []
    The item in arr[1]: [2, 3, [4, [5, 6]]] is a list
    ---- deep_reverse([2, 3, [4, [5, 6]]]) ---- START 
    ---- deep_reverse_func([2, 3, [4, [5, 6]]],0) ---- START
    ---- deep_reverse_func([2, 3, [4, [5, 6]]],1) ---- START
    ---- deep_reverse_func([2, 3, [4, [5, 6]]],2) ---- START
    ---- deep_reverse_func([2, 3, [4, [5, 6]]],3) ---- START
    Base case: []
    ---- deep_reverse_func([2, 3, [4, [5, 6]]],3) ---- END
    ---- deep_reverse_func([2, 3, [4, [5, 6]]],2) ---- CALL
    output: []
    The item in arr[2]: [4, [5, 6]] is a list
    ---- deep_reverse([4, [5, 6]]) ---- START 
    ---- deep_reverse_func([4, [5, 6]],0) ---- START
    ---- deep_reverse_func([4, [5, 6]],1) ---- START
    ---- deep_reverse_func([4, [5, 6]],2) ---- START
    Base case: []
    ---- deep_reverse_func([4, [5, 6]],2) ---- END
    ---- deep_reverse_func([4, [5, 6]],1) ---- CALL
    output: []
    The item in arr[1]: [5, 6] is a list
    ---- deep_reverse([5, 6]) ---- START 
    ---- deep_reverse_func([5, 6],0) ---- START
    ---- deep_reverse_func([5, 6],1) ---- START
    ---- deep_reverse_func([5, 6],2) ---- START
    Base case: []
    ---- deep_reverse_func([5, 6],2) ---- END
    ---- deep_reverse_func([5, 6],1) ---- CALL
    output: []
    to_append: 6
    output: [6]
    ---- deep_reverse_func([5, 6],1) ---- END
    ---- deep_reverse_func([5, 6],0) ---- CALL
    output: [6]
    to_append: 5
    output: [6, 5]
    ---- deep_reverse_func([5, 6],0) ---- END
    ---- deep_reverse([5, 6]) ---- END
    to_append: [6, 5]
    output: [[6, 5]]
    ---- deep_reverse_func([4, [5, 6]],1) ---- END
    ---- deep_reverse_func([4, [5, 6]],0) ---- CALL
    output: [[6, 5]]
    to_append: 4
    output: [[6, 5], 4]
    ---- deep_reverse_func([4, [5, 6]],0) ---- END
    ---- deep_reverse([4, [5, 6]]) ---- END
    to_append: [[6, 5], 4]
    output: [[[6, 5], 4]]
    ---- deep_reverse_func([2, 3, [4, [5, 6]]],2) ---- END
    ---- deep_reverse_func([2, 3, [4, [5, 6]]],1) ---- CALL
    output: [[[6, 5], 4]]
    to_append: 3
    output: [[[6, 5], 4], 3]
    ---- deep_reverse_func([2, 3, [4, [5, 6]]],1) ---- END
    ---- deep_reverse_func([2, 3, [4, [5, 6]]],0) ---- CALL
    output: [[[6, 5], 4], 3]
    to_append: 2
    output: [[[6, 5], 4], 3, 2]
    ---- deep_reverse_func([2, 3, [4, [5, 6]]],0) ---- END
    ---- deep_reverse([2, 3, [4, [5, 6]]]) ---- END
    to_append: [[[6, 5], 4], 3, 2]
    output: [[[[6, 5], 4], 3, 2]]
    ---- deep_reverse_func([1, [2, 3, [4, [5, 6]]]],1) ---- END
    ---- deep_reverse_func([1, [2, 3, [4, [5, 6]]]],0) ---- CALL
    output: [[[[6, 5], 4], 3, 2]]
    to_append: 1
    output: [[[[6, 5], 4], 3, 2], 1]
    ---- deep_reverse_func([1, [2, 3, [4, [5, 6]]]],0) ---- END
    ---- deep_reverse([1, [2, 3, [4, [5, 6]]]]) ---- END
    Pass



```python
arr =  [1, [2,3], 4, [5,6]]
solution = [ [6,5], 4, [3, 2], 1]
test_case = [arr, solution]
test_function(test_case)
```
