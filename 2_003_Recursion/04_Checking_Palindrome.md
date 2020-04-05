
# Palindrome

A **palindrome** is a word that is the reverse of itself—that is, it is the same word when read forwards and backwards.

For example:
*  "madam" is a palindrome
* "abba" is a palindrome
*  "cat" is not
*  "a" is a trivial case of a palindrome

The goal of this exercise is to use recursion to write a function `is_palindrome` that takes a string as input and checks whether that string is a palindrome. (Note that this problem can also be solved with a non-recursive solution, but that's not the point of this exercise.)


```python
def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.
    
    Args:
       input(str): input to be checked if it is palindrome
    """
    
    # TODO: Write your recursive palindrome checker here
    
    pass
        
```


```python
# Test Cases

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")

```

<span class="graffiti-highlight graffiti-id_crohunx-id_mwh78k9"><i></i><button>Hide Solution</button></span>


```python
# Solution

def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]

        # sub_input is input with first and last char removed
        sub_input = input[1:-1]

        return (first_char == last_char) and is_palindrome(sub_input)

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")

```


```python

```
