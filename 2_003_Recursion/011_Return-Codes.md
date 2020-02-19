
### Problem statement

In an encryption system where ASCII lower case letters represent numbers in the pattern `a=1, b=2, c=3...` and so on, find out all the codes that are possible for a given input number. 

**Example 1**

* `number = 123`
* `codes_possible = ["aw", "abc", "lc"]`

Explanation: The codes are for the following number:
         
* 1 . 23     = "aw"
* 1 . 2 . 3  = "abc"
* 12 . 3     = "lc"
    

**Example 2**  

* `number = 145`
* `codes_possible = ["ade", "ne"]`

Return the codes in a list. The order of codes in the list is not important.

*Note: you can assume that the input number will not contain any 0s*


```python
def all_codes(number):
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    TODO: complete this method and return a list with all possible codes for the input number
    """
    pass
```

<span class="graffiti-highlight graffiti-id_q8i2zj9-id_yrg0ir2"><i></i><button>Hide Solution</button></span>


```python
# Solution

def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember: 
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)

def all_codes(number):
    print('---- all_codes({}) ---- START '.format(number))
    if number == 0:
        print('Base case: {}'.format([""]))
        print('---- all_codes({}) ---- END '.format(number))
        return [""]
    
    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    output_100 = list()
    print('remainder: {}'.format(remainder))
    if remainder <= 26 and number > 9 :
        
        # get all codes for the remaining number
        output_100 = all_codes(number // 100)
        alphabet = get_alphabet(remainder)
        
        print('---- all_codes({}) ---- CALL FOR '.format(number))
        print('output_100: {}'.format(output_100))
        print('alphabet: {}'.format(alphabet))
        print('  for loop: output_100')
        for index, element in enumerate(output_100):
            print('\t - element: {}'.format(element))
            output_100[index] = element + alphabet
            print('\t - output_100[{}]: {} + {} = {}'.format(index, element, alphabet, output_100[index]))
    
    
    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number % 10
    
    # get all codes for the remaining number
    output_10 = all_codes(number // 10)
    alphabet = get_alphabet(remainder)
    print('---- all_codes({}) ---- CALL '.format(number))
    print('remainder: {}'.format(remainder))
    print('output_10: {}'.format(output_10))
    print('alphabet: {}'.format(alphabet))
    print('  for loop: output_10')
    for index, element in enumerate(output_10):
        print('\t - element: {}'.format(element))
        output_10[index] = element + alphabet
        print('\t - output_10[{}]: {} + {} = {}'.format(index, element, alphabet, output_10[index]))
        
    output = list()
    output.extend(output_100)
    output.extend(output_10)
    print('output_100: {}'.format(output_100))
    print('output_10: {}'.format(output_10))
    print('output: {}'.format(output))
    print('---- all_codes({}) ---- END '.format(number))
    return output
```


```python
def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]
    
    output = all_codes(number)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")
```


```python
number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)
```

    ---- all_codes(123) ---- START 
    remainder: 23
    ---- all_codes(1) ---- START 
    remainder: 1
    ---- all_codes(0) ---- START 
    Base case: ['']
    ---- all_codes(0) ---- END 
    ---- all_codes(1) ---- CALL 
    remainder: 1
    output_10: ['']
    alphabet: a
      for loop: output_10
    	 - element: 
    	 - output_10[0]:  + a = a
    output_100: []
    output_10: ['a']
    output: ['a']
    ---- all_codes(1) ---- END 
    ---- all_codes(123) ---- CALL FOR 
    output_100: ['a']
    alphabet: w
      for loop: output_100
    	 - element: a
    	 - output_100[0]: a + w = aw
    ---- all_codes(12) ---- START 
    remainder: 12
    ---- all_codes(0) ---- START 
    Base case: ['']
    ---- all_codes(0) ---- END 
    ---- all_codes(12) ---- CALL FOR 
    output_100: ['']
    alphabet: l
      for loop: output_100
    	 - element: 
    	 - output_100[0]:  + l = l
    ---- all_codes(1) ---- START 
    remainder: 1
    ---- all_codes(0) ---- START 
    Base case: ['']
    ---- all_codes(0) ---- END 
    ---- all_codes(1) ---- CALL 
    remainder: 1
    output_10: ['']
    alphabet: a
      for loop: output_10
    	 - element: 
    	 - output_10[0]:  + a = a
    output_100: []
    output_10: ['a']
    output: ['a']
    ---- all_codes(1) ---- END 
    ---- all_codes(12) ---- CALL 
    remainder: 2
    output_10: ['a']
    alphabet: b
      for loop: output_10
    	 - element: a
    	 - output_10[0]: a + b = ab
    output_100: ['l']
    output_10: ['ab']
    output: ['l', 'ab']
    ---- all_codes(12) ---- END 
    ---- all_codes(123) ---- CALL 
    remainder: 3
    output_10: ['l', 'ab']
    alphabet: c
      for loop: output_10
    	 - element: l
    	 - output_10[0]: l + c = lc
    	 - element: ab
    	 - output_10[1]: ab + c = abc
    output_100: ['aw']
    output_10: ['lc', 'abc']
    output: ['aw', 'lc', 'abc']
    ---- all_codes(123) ---- END 
    Pass



```python
number = 145
solution =  ['ade', 'ne']
test_case = [number, solution]
test_function(test_case)
```

    ---- all_codes(145) ---- START 
    remainder: 45
    ---- all_codes(14) ---- START 
    remainder: 14
    ---- all_codes(0) ---- START 
    Base case: ['']
    ---- all_codes(0) ---- END 
    ---- all_codes(14) ---- CALL 
    output_100: ['']
    ---- all_codes(1) ---- START 
    remainder: 1
    ---- all_codes(0) ---- START 
    Base case: ['']
    ---- all_codes(0) ---- END 
    Pass



```python
number = 1145
solution =  ['aade', 'ane', 'kde']
test_case = [number, solution]
test_function(test_case)
```

    Pass



```python
number = 4545
solution = ['dede']
test_case = [number, solution]
test_function(test_case)
```

    Pass

