
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
    print('---- return_permutations({},{}) ---- START: All permutation of the last {}'.format(string,index,len(string)-index))
    # Base Case: there are no permutations for an empty string
    if index >= len(string):
        print('Base case: [""]')
        print('---- return_permutations({},{}) ---- END'.format(string,index))
        return [""]
    
    small_output = return_permutations(string, index + 1)
    print('---- return_permutations({},{}) ---- CALL'.format(string,index))
    print('small_output: {}'.format(small_output))
    output = list()
    current_char = string[index]
    
    print('current char: {}'.format(current_char))
    # iterate over each permutation string received thus far
    # and place the current character at between different indices of the string
    print('for loop')
    for permutation in small_output:
        print('  permutation: {}'.format(permutation))
        print('  for loop')
        for i in range(len(small_output[0]) + 1):
            print('\t - i: {}'.format(i))
            new_permutation = permutation[0: i] + current_char + permutation[i:]
            print('\t new_permutation: {} + {} + {} = {}'.format(permutation[0: i], current_char, permutation[i:], new_permutation))
            output.append(new_permutation)
    print('output: {}'.format(output))
    print('---- return_permutations({},{}) ---- END'.format(string,index))
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

    ---- return_permutations(ab,0) ---- START: All permutation of the last 2
    ---- return_permutations(ab,1) ---- START: All permutation of the last 1
    ---- return_permutations(ab,2) ---- START: All permutation of the last 0
    Base case: [""]
    ---- return_permutations(ab,2) ---- END
    ---- return_permutations(ab,1) ---- CALL
    small_output: ['']
    current char: b
    for loop
      permutation: 
      for loop
    	 - i: 0
    	 new_permutation:  + b +  = b
    output: ['b']
    ---- return_permutations(ab,1) ---- END
    ---- return_permutations(ab,0) ---- CALL
    small_output: ['b']
    current char: a
    for loop
      permutation: b
      for loop
    	 - i: 0
    	 new_permutation:  + a + b = ab
    	 - i: 1
    	 new_permutation: b + a +  = ba
    output: ['ab', 'ba']
    ---- return_permutations(ab,0) ---- END
    Pass



```python
string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)
```

    ---- return_permutations(abc,0) ---- START: All permutation of the last 3
    ---- return_permutations(abc,1) ---- START: All permutation of the last 2
    ---- return_permutations(abc,2) ---- START: All permutation of the last 1
    ---- return_permutations(abc,3) ---- START: All permutation of the last 0
    Base case: [""]
    ---- return_permutations(abc,3) ---- END
    ---- return_permutations(abc,2) ---- CALL
    small_output: ['']
    current char: c
    for loop
      permutation: 
      for loop
    	 - i: 0
    	 new_permutation:  + c +  = c
    output: ['c']
    ---- return_permutations(abc,2) ---- END
    ---- return_permutations(abc,1) ---- CALL
    small_output: ['c']
    current char: b
    for loop
      permutation: c
      for loop
    	 - i: 0
    	 new_permutation:  + b + c = bc
    	 - i: 1
    	 new_permutation: c + b +  = cb
    output: ['bc', 'cb']
    ---- return_permutations(abc,1) ---- END
    ---- return_permutations(abc,0) ---- CALL
    small_output: ['bc', 'cb']
    current char: a
    for loop
      permutation: bc
      for loop
    	 - i: 0
    	 new_permutation:  + a + bc = abc
    	 - i: 1
    	 new_permutation: b + a + c = bac
    	 - i: 2
    	 new_permutation: bc + a +  = bca
      permutation: cb
      for loop
    	 - i: 0
    	 new_permutation:  + a + cb = acb
    	 - i: 1
    	 new_permutation: c + a + b = cab
    	 - i: 2
    	 new_permutation: cb + a +  = cba
    output: ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    ---- return_permutations(abc,0) ---- END
    Pass



```python
string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)
```

    ---- return_permutations(abcd,0) ---- START: All permutation of the last 4
    ---- return_permutations(abcd,1) ---- START: All permutation of the last 3
    ---- return_permutations(abcd,2) ---- START: All permutation of the last 2
    ---- return_permutations(abcd,3) ---- START: All permutation of the last 1
    ---- return_permutations(abcd,4) ---- START: All permutation of the last 0
    Base case: [""]
    ---- return_permutations(abcd,4) ---- END
    ---- return_permutations(abcd,3) ---- CALL
    small_output: ['']
    current char: d
    for loop
      permutation: 
      for loop
    	 - i: 0
    	 new_permutation:  + d +  = d
    output: ['d']
    ---- return_permutations(abcd,3) ---- END
    ---- return_permutations(abcd,2) ---- CALL
    small_output: ['d']
    current char: c
    for loop
      permutation: d
      for loop
    	 - i: 0
    	 new_permutation:  + c + d = cd
    	 - i: 1
    	 new_permutation: d + c +  = dc
    output: ['cd', 'dc']
    ---- return_permutations(abcd,2) ---- END
    ---- return_permutations(abcd,1) ---- CALL
    small_output: ['cd', 'dc']
    current char: b
    for loop
      permutation: cd
      for loop
    	 - i: 0
    	 new_permutation:  + b + cd = bcd
    	 - i: 1
    	 new_permutation: c + b + d = cbd
    	 - i: 2
    	 new_permutation: cd + b +  = cdb
      permutation: dc
      for loop
    	 - i: 0
    	 new_permutation:  + b + dc = bdc
    	 - i: 1
    	 new_permutation: d + b + c = dbc
    	 - i: 2
    	 new_permutation: dc + b +  = dcb
    output: ['bcd', 'cbd', 'cdb', 'bdc', 'dbc', 'dcb']
    ---- return_permutations(abcd,1) ---- END
    ---- return_permutations(abcd,0) ---- CALL
    small_output: ['bcd', 'cbd', 'cdb', 'bdc', 'dbc', 'dcb']
    current char: a
    for loop
      permutation: bcd
      for loop
    	 - i: 0
    	 new_permutation:  + a + bcd = abcd
    	 - i: 1
    	 new_permutation: b + a + cd = bacd
    	 - i: 2
    	 new_permutation: bc + a + d = bcad
    	 - i: 3
    	 new_permutation: bcd + a +  = bcda
      permutation: cbd
      for loop
    	 - i: 0
    	 new_permutation:  + a + cbd = acbd
    	 - i: 1
    	 new_permutation: c + a + bd = cabd
    	 - i: 2
    	 new_permutation: cb + a + d = cbad
    	 - i: 3
    	 new_permutation: cbd + a +  = cbda
      permutation: cdb
      for loop
    	 - i: 0
    	 new_permutation:  + a + cdb = acdb
    	 - i: 1
    	 new_permutation: c + a + db = cadb
    	 - i: 2
    	 new_permutation: cd + a + b = cdab
    	 - i: 3
    	 new_permutation: cdb + a +  = cdba
      permutation: bdc
      for loop
    	 - i: 0
    	 new_permutation:  + a + bdc = abdc
    	 - i: 1
    	 new_permutation: b + a + dc = badc
    	 - i: 2
    	 new_permutation: bd + a + c = bdac
    	 - i: 3
    	 new_permutation: bdc + a +  = bdca
      permutation: dbc
      for loop
    	 - i: 0
    	 new_permutation:  + a + dbc = adbc
    	 - i: 1
    	 new_permutation: d + a + bc = dabc
    	 - i: 2
    	 new_permutation: db + a + c = dbac
    	 - i: 3
    	 new_permutation: dbc + a +  = dbca
      permutation: dcb
      for loop
    	 - i: 0
    	 new_permutation:  + a + dcb = adcb
    	 - i: 1
    	 new_permutation: d + a + cb = dacb
    	 - i: 2
    	 new_permutation: dc + a + b = dcab
    	 - i: 3
    	 new_permutation: dcb + a +  = dcba
    output: ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
    ---- return_permutations(abcd,0) ---- END
    Pass



```python

```
