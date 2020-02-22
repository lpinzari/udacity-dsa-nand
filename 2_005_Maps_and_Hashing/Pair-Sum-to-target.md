
### Problem statement

Given an `input_list` and a `target`, return the indices of pair of integers in the list that sum to the target. The best solution takes O(n) time. You can assume that the list does not have any duplicates.

For e.g. `input_list = [1, 5, 9, 7]` and `target = 8`, the answer would be `[0, 3]` 


```python
def pair_sum_to_zero(input_list, target):
    # TODO: Write pair sum to zero function
    index_dict = dict()
    for index, element in enumerate(input_list):
        if target - element in index_dict:
            return [index_dict[target - element], index]
        index_dict[element] = index
```


```python
def test_function(test_case):
    output = pair_sum_to_zero(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")
```


```python
test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
test_function(test_case_1)
```

    [0, 3]
    Pass



```python
test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
test_function(test_case_2)
```

    [0, 7]
    Pass



```python
test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
test_function(test_case_3)
```

    [0, 4]
    Pass


<span class="graffiti-highlight graffiti-id_snm0ke6-id_tv0tye7"><i></i><button>Hide Solution</button></span>


```python
def pair_sum_to_zero(input_list, target):
    index_dict = dict()
    for index, element in enumerate(input_list):
        if target - element in index_dict:
            return [index_dict[target - element], index]
        index_dict[element] = index
        

```
