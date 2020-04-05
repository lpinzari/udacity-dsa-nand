
# Reversing a String

The goal in this notebook will be to get practice with a problem that is frequently solved by recursion: Reversing a string.

Note that Python has a built-in function that you could use for this, but the goal here is to avoid that and understand how it can be done using recursion instead.


```python
# Code

def reverse_string(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that is the reverse of input
    """
    
    # TODO: Write your recursive string reverser solution here
    
    pass
```


```python
# Test Cases
    
print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")
```

<span class="graffiti-highlight graffiti-id_4uzxsts-id_3o4r993"><i></i><button>Hide Solution</button></span>


```python
# Solution

def reverse_string(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that us reversed of input
    """
    if len(input) == 0:
        return ""
    else:
        first_char = input[0]
        the_rest = slice(1, None)
        sub_string = input[the_rest]
        reversed_substring = reverse_string(sub_string)
        return reversed_substring + first_char

print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")

```


```python

```
