
### Problem Statement

Given list of integers that contain numbers in random order, write a program to find the longest possible sub sequence of consecutive numbers in the array. Return this subsequence in sorted order. The solution must take O(n) time

For e.g. given the list `5, 4, 7, 10, 1, 3, 55, 2`, the output should be `1, 2, 3, 4, 5`

*Note- If two arrays are of equal length return the array whose index of smallest element comes first.*




```python
def longest_consecutive_subsequence(input_list):
    # TODO: Write longest consecutive subsequence solution
    
    # iterate over the list and store element in a suitable data structure
    # Note that all the consecutive subsequences is a partition of the list
    # if the maximum length is one it means there are no consecutive numbers
    # traverse / go over the data structure in a reasonable order to determine the solution
    # note: the elements in the input_list are unique (i.e. no duplicates)
    element_dict = dict()

    for index, element in enumerate(input_list):
        element_dict[element] = index
        
    print('List input:{}'.format(element_dict))
    # maximum length of the sequence
    max_length = -1
    
    # the length of the sequence can be at most equal to the size of the list
    starts_at = len(input_list)

    for index, element in enumerate(input_list):
        current_starts = index
        # set the index of the current element to -1 (it has been visited)
        element_dict[element] = -1
        
        # we are going to compute the longest sequence for this element
        print('current_starts: {}'.format(current_starts))
        print(element_dict)
        current_count = 1

        # Calculate the size of the longest subsequence for the current element
        # downwards < element < upwards
        
        # check upwards for the next consecutive integer.
        current = element + 1

        # if the element is in the dictionary (i.e in the array) and it has not been visited in a previous step
        # (i.e the element has not been assigned to a subsequence yet.)
        while current in element_dict and element_dict[current] > 0:
            current_count += 1
            element_dict[current] = -1
            # check for the next integer
            current = current + 1

        # check downwards
        current = element - 1
        while current in element_dict and element_dict[current] > 0:
            # since we are going downwards we must update the current start of the sequence
            # it is the index of the smallest number in the sequence
            current_starts = element_dict[current]
            current_count += 1
            element_dict[current] = -1
            current = current - 1
            
            
        # if the current length of the sequence is greater than the maximum found so far
        if current_count >= max_length:
            # if the current length == maximum and index of the first number in the sequence > the index
            # of the longest sequence found so far than exit the for loop.
            if current_count == max_length and current_starts > starts_at:
                continue
            # update the index of the first element of the longest subsequence
            starts_at = current_starts
            print('stats_at: {}'.format(starts_at))
            max_length = current_count
            
        print(element_dict)
        start_element = input_list[starts_at]
        for element in range(start_element, start_element + max_length):
            print(element)
        # end for
    
    # starting at the first element of the list return all the consecutive numbers up to the maximum length
    start_element = input_list[starts_at]
    return [element for element in range(start_element, start_element + max_length)]

```


```python
def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")
    
```


```python
test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)
```

    List input:{5: 0, 4: 1, 7: 2, 10: 3, 1: 4, 3: 5, 55: 6, 2: 7}
    current_starts: 0
    {5: -1, 4: 1, 7: 2, 10: 3, 1: 4, 3: 5, 55: 6, 2: 7}
    stats_at: 4
    {5: -1, 4: -1, 7: 2, 10: 3, 1: -1, 3: -1, 55: 6, 2: -1}
    1
    2
    3
    4
    5
    current_starts: 1
    {5: -1, 4: -1, 7: 2, 10: 3, 1: -1, 3: -1, 55: 6, 2: -1}
    {5: -1, 4: -1, 7: 2, 10: 3, 1: -1, 3: -1, 55: 6, 2: -1}
    1
    2
    3
    4
    5
    current_starts: 2
    {5: -1, 4: -1, 7: -1, 10: 3, 1: -1, 3: -1, 55: 6, 2: -1}
    {5: -1, 4: -1, 7: -1, 10: 3, 1: -1, 3: -1, 55: 6, 2: -1}
    1
    2
    3
    4
    5
    current_starts: 3
    {5: -1, 4: -1, 7: -1, 10: -1, 1: -1, 3: -1, 55: 6, 2: -1}
    {5: -1, 4: -1, 7: -1, 10: -1, 1: -1, 3: -1, 55: 6, 2: -1}
    1
    2
    3
    4
    5
    current_starts: 4
    {5: -1, 4: -1, 7: -1, 10: -1, 1: -1, 3: -1, 55: 6, 2: -1}
    {5: -1, 4: -1, 7: -1, 10: -1, 1: -1, 3: -1, 55: 6, 2: -1}
    1
    2
    3
    4
    5
    current_starts: 5
    {5: -1, 4: -1, 7: -1, 10: -1, 1: -1, 3: -1, 55: 6, 2: -1}
    {5: -1, 4: -1, 7: -1, 10: -1, 1: -1, 3: -1, 55: 6, 2: -1}
    1
    2
    3
    4
    5
    current_starts: 6
    {5: -1, 4: -1, 7: -1, 10: -1, 1: -1, 3: -1, 55: -1, 2: -1}
    {5: -1, 4: -1, 7: -1, 10: -1, 1: -1, 3: -1, 55: -1, 2: -1}
    1
    2
    3
    4
    5
    current_starts: 7
    {5: -1, 4: -1, 7: -1, 10: -1, 1: -1, 3: -1, 55: -1, 2: -1}
    {5: -1, 4: -1, 7: -1, 10: -1, 1: -1, 3: -1, 55: -1, 2: -1}
    1
    2
    3
    4
    5
    Pass



```python
test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6 ], [8, 9, 10, 11, 12]]
test_function(test_case_2)
```

    List input:{2: 0, 12: 1, 9: 2, 16: 3, 10: 4, 5: 5, 3: 6, 20: 7, 25: 8, 11: 9, 1: 10, 8: 11, 6: 12}
    current_starts: 0
    {2: -1, 12: 1, 9: 2, 16: 3, 10: 4, 5: 5, 3: 6, 20: 7, 25: 8, 11: 9, 1: 10, 8: 11, 6: 12}
    stats_at: 10
    {2: -1, 12: 1, 9: 2, 16: 3, 10: 4, 5: 5, 3: -1, 20: 7, 25: 8, 11: 9, 1: -1, 8: 11, 6: 12}
    1
    2
    3
    current_starts: 1
    {2: -1, 12: -1, 9: 2, 16: 3, 10: 4, 5: 5, 3: -1, 20: 7, 25: 8, 11: 9, 1: -1, 8: 11, 6: 12}
    stats_at: 11
    {2: -1, 12: -1, 9: -1, 16: 3, 10: -1, 5: 5, 3: -1, 20: 7, 25: 8, 11: -1, 1: -1, 8: -1, 6: 12}
    8
    9
    10
    11
    12
    current_starts: 2
    {2: -1, 12: -1, 9: -1, 16: 3, 10: -1, 5: 5, 3: -1, 20: 7, 25: 8, 11: -1, 1: -1, 8: -1, 6: 12}
    {2: -1, 12: -1, 9: -1, 16: 3, 10: -1, 5: 5, 3: -1, 20: 7, 25: 8, 11: -1, 1: -1, 8: -1, 6: 12}
    8
    9
    10
    11
    12
    current_starts: 3
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: 5, 3: -1, 20: 7, 25: 8, 11: -1, 1: -1, 8: -1, 6: 12}
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: 5, 3: -1, 20: 7, 25: 8, 11: -1, 1: -1, 8: -1, 6: 12}
    8
    9
    10
    11
    12
    current_starts: 4
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: 5, 3: -1, 20: 7, 25: 8, 11: -1, 1: -1, 8: -1, 6: 12}
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: 5, 3: -1, 20: 7, 25: 8, 11: -1, 1: -1, 8: -1, 6: 12}
    8
    9
    10
    11
    12
    current_starts: 5
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: 7, 25: 8, 11: -1, 1: -1, 8: -1, 6: 12}
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: 7, 25: 8, 11: -1, 1: -1, 8: -1, 6: -1}
    8
    9
    10
    11
    12
    current_starts: 6
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: 7, 25: 8, 11: -1, 1: -1, 8: -1, 6: -1}
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: 7, 25: 8, 11: -1, 1: -1, 8: -1, 6: -1}
    8
    9
    10
    11
    12
    current_starts: 7
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: 8, 11: -1, 1: -1, 8: -1, 6: -1}
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: 8, 11: -1, 1: -1, 8: -1, 6: -1}
    8
    9
    10
    11
    12
    current_starts: 8
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: -1, 11: -1, 1: -1, 8: -1, 6: -1}
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: -1, 11: -1, 1: -1, 8: -1, 6: -1}
    8
    9
    10
    11
    12
    current_starts: 9
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: -1, 11: -1, 1: -1, 8: -1, 6: -1}
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: -1, 11: -1, 1: -1, 8: -1, 6: -1}
    8
    9
    10
    11
    12
    current_starts: 10
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: -1, 11: -1, 1: -1, 8: -1, 6: -1}
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: -1, 11: -1, 1: -1, 8: -1, 6: -1}
    8
    9
    10
    11
    12
    current_starts: 11
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: -1, 11: -1, 1: -1, 8: -1, 6: -1}
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: -1, 11: -1, 1: -1, 8: -1, 6: -1}
    8
    9
    10
    11
    12
    current_starts: 12
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: -1, 11: -1, 1: -1, 8: -1, 6: -1}
    {2: -1, 12: -1, 9: -1, 16: -1, 10: -1, 5: -1, 3: -1, 20: -1, 25: -1, 11: -1, 1: -1, 8: -1, 6: -1}
    8
    9
    10
    11
    12
    Pass



```python
test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)
```

    List input:{0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    current_starts: 0
    {0: -1, 1: 1, 2: 2, 3: 3, 4: 4}
    stats_at: 0
    {0: -1, 1: -1, 2: -1, 3: -1, 4: -1}
    0
    1
    2
    3
    4
    current_starts: 1
    {0: -1, 1: -1, 2: -1, 3: -1, 4: -1}
    {0: -1, 1: -1, 2: -1, 3: -1, 4: -1}
    0
    1
    2
    3
    4
    current_starts: 2
    {0: -1, 1: -1, 2: -1, 3: -1, 4: -1}
    {0: -1, 1: -1, 2: -1, 3: -1, 4: -1}
    0
    1
    2
    3
    4
    current_starts: 3
    {0: -1, 1: -1, 2: -1, 3: -1, 4: -1}
    {0: -1, 1: -1, 2: -1, 3: -1, 4: -1}
    0
    1
    2
    3
    4
    current_starts: 4
    {0: -1, 1: -1, 2: -1, 3: -1, 4: -1}
    {0: -1, 1: -1, 2: -1, 3: -1, 4: -1}
    0
    1
    2
    3
    4
    Pass


<span class="graffiti-highlight graffiti-id_et1ek54-id_r15x1vg"><i></i><button>Hide Solution</button></span>


```python
def longest_consecutive_subsequence(input_list):
    element_dict = dict()

    for index, element in enumerate(input_list):
        element_dict[element] = index
        
    print(element_dict)
    max_length = -1
    starts_at = len(input_list)

    for index, element in enumerate(input_list):
        current_starts = index
        element_dict[element] = -1

        current_count = 1

        # check upwards
        current = element + 1

        while current in element_dict and element_dict[current] > 0:
            current_count += 1
            element_dict[current] = -1
            current = current + 1

        # check downwards
        current = element - 1
        while current in element_dict and element_dict[current] > 0:
            current_starts = element_dict[current]
            current_count += 1
            element_dict[current] = -1
            current = current - 1

        if current_count >= max_length:
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts
            max_length = current_count

    start_element = input_list[starts_at]
    return [element for element in range(start_element, start_element + max_length)]




```
