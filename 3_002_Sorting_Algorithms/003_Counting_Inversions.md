
# Counting Inversions

The number of *inversions* in a disordered list is the number of pairs of elements that are inverted (out of order) in the list.  

Here are some examples: 
  - [0,1] has 0 inversions
  - [2,1] has 1 inversion (2,1)
  - [3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
  - [7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
  
The number of inversions can also be thought of in the following manner. 

>Given an array `arr[0 ... n-1]` of `n` distinct positive integers, for indices `i and j`, if `i < j` and `arr[i] > arr[j]` then the pair `(i, j)` is called an inversion of `arr`.

## Problem statement

Write a function, `count_inversions`, that takes an array (or Python list) as input, and returns a count of the total number of inversions present in the input.

Mergesort provides an efficient way to solve this problem.


```python
def count_inversions(arr):
    # TODO: NAIVE APPROACH
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

arr = [2, 5, 1, 3, 4]
print(count_inversions(arr)) # 4

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
print(count_inversions(arr)) # 26

```

    4
    26


<span class="graffiti-highlight graffiti-id_8809fp2-id_8br31oi"><i></i><button>Hide Solution</button></span>


```python
def count_inversions(arr):
    start_index = 0
    end_index = len(arr) - 1
    output = inversion_count_func(arr, start_index, end_index)
    return output


def inversion_count_func(arr, start_index, end_index):

    # Base case: single element
    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2
    
    print('-------START: \t inversion_count(l-half) ({},{})'.format(start_index, mid_index))
    
    # find number of inversions in left-half
    left_answer = inversion_count_func(arr, start_index, mid_index)
    
    print('---------END: \t inversion_count(l-half) ({},{}) \t left: {}'.format(start_index, mid_index,left_answer))
    
    
    print('-------START: \t inversion_count(r-half) ({},{})'.format(mid_index + 1, end_index))
    
    # find number of inversions in right-half
    right_answer = inversion_count_func(arr, mid_index + 1, end_index)
    
    print('---------END: \t inversion_count(r-half) ({},{}) \t right: {}'.format(mid_index + 1, end_index,right_answer))

    output = left_answer + right_answer
    print('              \t                         ({},{}) \t left + right: {}'.format(start_index,end_index,output))
    
    print('array: {}'.format(arr))
    print('merge({},{}) ({},{})'.format(start_index,mid_index,mid_index+1,end_index))
    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(arr, start_index, mid_index, mid_index + 1, end_index)
    print('sorted: {} \t count: {}'.format(arr,output))
    return output


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_index = start_one
    right_index = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_index] <= arr[right_index]:
            output_list[index] = arr[left_index]
            left_index += 1

        else:
            count = count + (end_one - left_index + 1)           # left > right hence it's an inversion
            output_list[index] = arr[right_index]
            right_index += 1

        index = index + 1

        if left_index > end_one:
            for i in range(right_index, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_index > end_two:
            for i in range(left_index, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break

    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    return count
```


```python
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")

```


```python
arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)
```

    -------START: 	 inversion_count(l-half) (0,2)
    -------START: 	 inversion_count(l-half) (0,1)
    -------START: 	 inversion_count(l-half) (0,0)
    ---------END: 	 inversion_count(l-half) (0,0) 	 left: 0
    -------START: 	 inversion_count(r-half) (1,1)
    ---------END: 	 inversion_count(r-half) (1,1) 	 right: 0
                  	                         (0,1) 	 left + right: 0
    array: [2, 5, 1, 3, 4]
    merge(0,0) (1,1)
    sorted: [2, 5, 1, 3, 4] 	 count: 0
    ---------END: 	 inversion_count(l-half) (0,1) 	 left: 0
    -------START: 	 inversion_count(r-half) (2,2)
    ---------END: 	 inversion_count(r-half) (2,2) 	 right: 0
                  	                         (0,2) 	 left + right: 0
    array: [2, 5, 1, 3, 4]
    merge(0,1) (2,2)
    sorted: [1, 2, 5, 3, 4] 	 count: 2
    ---------END: 	 inversion_count(l-half) (0,2) 	 left: 2
    -------START: 	 inversion_count(r-half) (3,4)
    -------START: 	 inversion_count(l-half) (3,3)
    ---------END: 	 inversion_count(l-half) (3,3) 	 left: 0
    -------START: 	 inversion_count(r-half) (4,4)
    ---------END: 	 inversion_count(r-half) (4,4) 	 right: 0
                  	                         (3,4) 	 left + right: 0
    array: [1, 2, 5, 3, 4]
    merge(3,3) (4,4)
    sorted: [1, 2, 5, 3, 4] 	 count: 0
    ---------END: 	 inversion_count(r-half) (3,4) 	 right: 0
                  	                         (0,4) 	 left + right: 2
    array: [1, 2, 5, 3, 4]
    merge(0,2) (3,4)
    sorted: [1, 2, 3, 4, 5] 	 count: 4
    Pass



```python
arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)
```

    -------START: 	 inversion_count(l-half) (0,4)
    -------START: 	 inversion_count(l-half) (0,2)
    -------START: 	 inversion_count(l-half) (0,1)
    -------START: 	 inversion_count(l-half) (0,0)
    ---------END: 	 inversion_count(l-half) (0,0) 	 left: 0
    -------START: 	 inversion_count(r-half) (1,1)
    ---------END: 	 inversion_count(r-half) (1,1) 	 right: 0
                  	                         (0,1) 	 left + right: 0
    array: [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
    merge(0,0) (1,1)
    sorted: [54, 99, 49, 22, 37, 18, 22, 90, 86, 33] 	 count: 0
    ---------END: 	 inversion_count(l-half) (0,1) 	 left: 0
    -------START: 	 inversion_count(r-half) (2,2)
    ---------END: 	 inversion_count(r-half) (2,2) 	 right: 0
                  	                         (0,2) 	 left + right: 0
    array: [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
    merge(0,1) (2,2)
    sorted: [49, 54, 99, 22, 37, 18, 22, 90, 86, 33] 	 count: 2
    ---------END: 	 inversion_count(l-half) (0,2) 	 left: 2
    -------START: 	 inversion_count(r-half) (3,4)
    -------START: 	 inversion_count(l-half) (3,3)
    ---------END: 	 inversion_count(l-half) (3,3) 	 left: 0
    -------START: 	 inversion_count(r-half) (4,4)
    ---------END: 	 inversion_count(r-half) (4,4) 	 right: 0
                  	                         (3,4) 	 left + right: 0
    array: [49, 54, 99, 22, 37, 18, 22, 90, 86, 33]
    merge(3,3) (4,4)
    sorted: [49, 54, 99, 22, 37, 18, 22, 90, 86, 33] 	 count: 0
    ---------END: 	 inversion_count(r-half) (3,4) 	 right: 0
                  	                         (0,4) 	 left + right: 2
    array: [49, 54, 99, 22, 37, 18, 22, 90, 86, 33]
    merge(0,2) (3,4)
    sorted: [22, 37, 49, 54, 99, 18, 22, 90, 86, 33] 	 count: 8
    ---------END: 	 inversion_count(l-half) (0,4) 	 left: 8
    -------START: 	 inversion_count(r-half) (5,9)
    -------START: 	 inversion_count(l-half) (5,7)
    -------START: 	 inversion_count(l-half) (5,6)
    -------START: 	 inversion_count(l-half) (5,5)
    ---------END: 	 inversion_count(l-half) (5,5) 	 left: 0
    -------START: 	 inversion_count(r-half) (6,6)
    ---------END: 	 inversion_count(r-half) (6,6) 	 right: 0
                  	                         (5,6) 	 left + right: 0
    array: [22, 37, 49, 54, 99, 18, 22, 90, 86, 33]
    merge(5,5) (6,6)
    sorted: [22, 37, 49, 54, 99, 18, 22, 90, 86, 33] 	 count: 0
    ---------END: 	 inversion_count(l-half) (5,6) 	 left: 0
    -------START: 	 inversion_count(r-half) (7,7)
    ---------END: 	 inversion_count(r-half) (7,7) 	 right: 0
                  	                         (5,7) 	 left + right: 0
    array: [22, 37, 49, 54, 99, 18, 22, 90, 86, 33]
    merge(5,6) (7,7)
    sorted: [22, 37, 49, 54, 99, 18, 22, 90, 86, 33] 	 count: 0
    ---------END: 	 inversion_count(l-half) (5,7) 	 left: 0
    -------START: 	 inversion_count(r-half) (8,9)
    -------START: 	 inversion_count(l-half) (8,8)
    ---------END: 	 inversion_count(l-half) (8,8) 	 left: 0
    -------START: 	 inversion_count(r-half) (9,9)
    ---------END: 	 inversion_count(r-half) (9,9) 	 right: 0
                  	                         (8,9) 	 left + right: 0
    array: [22, 37, 49, 54, 99, 18, 22, 90, 86, 33]
    merge(8,8) (9,9)
    sorted: [22, 37, 49, 54, 99, 18, 22, 90, 33, 86] 	 count: 1
    ---------END: 	 inversion_count(r-half) (8,9) 	 right: 1
                  	                         (5,9) 	 left + right: 1
    array: [22, 37, 49, 54, 99, 18, 22, 90, 33, 86]
    merge(5,7) (8,9)
    sorted: [22, 37, 49, 54, 99, 18, 22, 33, 86, 90] 	 count: 3
    ---------END: 	 inversion_count(r-half) (5,9) 	 right: 3
                  	                         (0,9) 	 left + right: 11
    array: [22, 37, 49, 54, 99, 18, 22, 33, 86, 90]
    merge(0,4) (5,9)
    sorted: [18, 22, 22, 33, 37, 49, 54, 86, 90, 99] 	 count: 26
    Pass



```python
arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)
```

    -------START: 	 inversion_count(l-half) (0,4)
    -------START: 	 inversion_count(l-half) (0,2)
    -------START: 	 inversion_count(l-half) (0,1)
    -------START: 	 inversion_count(l-half) (0,0)
    ---------END: 	 inversion_count(l-half) (0,0) 	 left: 0
    -------START: 	 inversion_count(r-half) (1,1)
    ---------END: 	 inversion_count(r-half) (1,1) 	 right: 0
                  	                         (0,1) 	 left + right: 0
    array: [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
    merge(0,0) (1,1)
    sorted: [1, 2, 4, 2, 3, 11, 22, 99, 108, 389] 	 count: 0
    ---------END: 	 inversion_count(l-half) (0,1) 	 left: 0
    -------START: 	 inversion_count(r-half) (2,2)
    ---------END: 	 inversion_count(r-half) (2,2) 	 right: 0
                  	                         (0,2) 	 left + right: 0
    array: [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
    merge(0,1) (2,2)
    sorted: [1, 2, 4, 2, 3, 11, 22, 99, 108, 389] 	 count: 0
    ---------END: 	 inversion_count(l-half) (0,2) 	 left: 0
    -------START: 	 inversion_count(r-half) (3,4)
    -------START: 	 inversion_count(l-half) (3,3)
    ---------END: 	 inversion_count(l-half) (3,3) 	 left: 0
    -------START: 	 inversion_count(r-half) (4,4)
    ---------END: 	 inversion_count(r-half) (4,4) 	 right: 0
                  	                         (3,4) 	 left + right: 0
    array: [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
    merge(3,3) (4,4)
    sorted: [1, 2, 4, 2, 3, 11, 22, 99, 108, 389] 	 count: 0
    ---------END: 	 inversion_count(r-half) (3,4) 	 right: 0
                  	                         (0,4) 	 left + right: 0
    array: [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
    merge(0,2) (3,4)
    sorted: [1, 2, 2, 3, 4, 11, 22, 99, 108, 389] 	 count: 2
    ---------END: 	 inversion_count(l-half) (0,4) 	 left: 2
    -------START: 	 inversion_count(r-half) (5,9)
    -------START: 	 inversion_count(l-half) (5,7)
    -------START: 	 inversion_count(l-half) (5,6)
    -------START: 	 inversion_count(l-half) (5,5)
    ---------END: 	 inversion_count(l-half) (5,5) 	 left: 0
    -------START: 	 inversion_count(r-half) (6,6)
    ---------END: 	 inversion_count(r-half) (6,6) 	 right: 0
                  	                         (5,6) 	 left + right: 0
    array: [1, 2, 2, 3, 4, 11, 22, 99, 108, 389]
    merge(5,5) (6,6)
    sorted: [1, 2, 2, 3, 4, 11, 22, 99, 108, 389] 	 count: 0
    ---------END: 	 inversion_count(l-half) (5,6) 	 left: 0
    -------START: 	 inversion_count(r-half) (7,7)
    ---------END: 	 inversion_count(r-half) (7,7) 	 right: 0
                  	                         (5,7) 	 left + right: 0
    array: [1, 2, 2, 3, 4, 11, 22, 99, 108, 389]
    merge(5,6) (7,7)
    sorted: [1, 2, 2, 3, 4, 11, 22, 99, 108, 389] 	 count: 0
    ---------END: 	 inversion_count(l-half) (5,7) 	 left: 0
    -------START: 	 inversion_count(r-half) (8,9)
    -------START: 	 inversion_count(l-half) (8,8)
    ---------END: 	 inversion_count(l-half) (8,8) 	 left: 0
    -------START: 	 inversion_count(r-half) (9,9)
    ---------END: 	 inversion_count(r-half) (9,9) 	 right: 0
                  	                         (8,9) 	 left + right: 0
    array: [1, 2, 2, 3, 4, 11, 22, 99, 108, 389]
    merge(8,8) (9,9)
    sorted: [1, 2, 2, 3, 4, 11, 22, 99, 108, 389] 	 count: 0
    ---------END: 	 inversion_count(r-half) (8,9) 	 right: 0
                  	                         (5,9) 	 left + right: 0
    array: [1, 2, 2, 3, 4, 11, 22, 99, 108, 389]
    merge(5,7) (8,9)
    sorted: [1, 2, 2, 3, 4, 11, 22, 99, 108, 389] 	 count: 0
    ---------END: 	 inversion_count(r-half) (5,9) 	 right: 0
                  	                         (0,9) 	 left + right: 2
    array: [1, 2, 2, 3, 4, 11, 22, 99, 108, 389]
    merge(0,4) (5,9)
    sorted: [1, 2, 2, 3, 4, 11, 22, 99, 108, 389] 	 count: 2
    Pass



```python

```
