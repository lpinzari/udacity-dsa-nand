
### Problem Statement

Given an input string, return all permutations of the string in an array.

**Example 1:**
* `string = 'ab'`
* `output = ['ab', 'ba']`

**Example 2:**
* `string = 'abc'`
* `output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']`



```python

```


```python
def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    pass
```

<span class="graffiti-highlight graffiti-id_2d0q2u5-id_vkbq25t"><i></i><button>Hide Solution</button></span>


```python
# Solution
def permutations(string):
    return return_permutations(string, 0)
    
def return_permutations(string, index):
    # Base Case
    if index >= len(string):
        return [""]
    
    small_output = return_permutations(string, index + 1)
    
    output = list()
    current_char = string[index]
    
    # iterate over each permutation string received thus far
    # and place the current character at between different indices of the string
    for permutation in small_output:
        for index in range(len(small_output[0]) + 1):
            new_permutation = permutation[0: index] + current_char + permutation[index:]
            output.append(new_permutation)
    return output

```


```python
def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")
```


```python
string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)
```

    Pass



```python
string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)
```

    Pass



```python
string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)
```

    Pass

