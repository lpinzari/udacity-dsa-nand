# Arithmetic Operators

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Mod (the remainder after dividing)
- `**` Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
- `//` Divides and rounds down to the nearest integer

The usual order of mathematical operations holds in Python, which you can review in this [Math Forum](http://mathforum.org/dr.math/faq/faq.order.operations.html) page if needed.

Bitwise operators are special operators in Python that you can learn more about here [Bitwise](https://wiki.python.org/moin/BitwiseOperators) if you'd like.

# Variables

1. Only use ordinary letters, numbers and underscores in your variable names. They can’t have spaces, and need to start with a letter or underscore.

2. You can’t use **reserved words** or built-in identifiers that have important purposes in Python, which you’ll learn about throughout this course. A list of python reserved words is described [here](https://pentangle.net/python/handbook/node52.html). Creating names that are descriptive of the values often will help you avoid using any of these words.

3. The pythonic way to name variables is to use all lowercase letters and underscores to separate words.

**YES**

```python
my_height = 58
my_lat = 40
my_long = 105
```

**NO**

```python
my height = 58
MYLONG = 40
MyLat = 105
```

Though the last two of these would work in python, they are not pythonic ways to name variables. The way we name variables is called snake case, because we tend to connect the words with underscores.

# Assignment Operators

Assignment operators are used in Python to assign values to variables.

`a = 5` is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.

There are various compound operators in Python like `a += 5` that adds to the variable and later assigns the same. It is equivalent to `a = a + 5`.

You can find some practice with much of what we have already covered [here](https://www.programiz.com/python-programming/operators).

# Integers and Floats
There are two Python data types that could be used for numeric values:

- int - for integer values
- float - for decimal or floating point values
You can create a value that follows the data type by using the following syntax:

```python
x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0
```
You can check the type by using the `type` function:

```python
>>> print(type(x))
int
>>> print(type(y))
float
```
Because the float, or approximation, for 0.1 is actually slightly more than 0.1, when we add several of them together we can see the difference between the mathematically correct answer and the one that Python creates.

```python
>>> print(.1 + .1 + .1 == .3)
False
```

You can find more about this topic [here](https://docs.python.org/3/tutorial/floatingpoint.html)

# Python Best Practices
For all the best practices, see the [PEP8](https://www.python.org/dev/peps/pep-0008/) Guidelines.

You can use the atom package [linter-python-pep8](https://atom.io/packages/linter-python-pep8) to use pep8 within your own programming environment in the Atom text editor, but more on this later. You should limit each line of code to 80 characters, though 99 is okay for certain use cases.

# Divide By Zero?
What happens if you divide by zero in Python? Try it out! Test run this code and see what happens. `print(5/0)`

```python
Traceback (most recent call last):
  File "/tmp/vmuser_tnryxwdmhw/quiz.py", line 1, in <module>
    print(5/0)

ZeroDivisionError: division by zero
```

`Traceback` means "What was the programming doing when it broke"! This part is usually less helpful than the very last line of your error. Though you can dig through the rest of the error, looking at just the final line `ZeroDivisionError`, and the message says we divided by zero. Python is enforcing the rules of arithmetic!

In general, there are two types of errors to look out for

- **Exceptions**
- **Syntax**
An Exception is a problem that occurs when the code is running, but a 'Syntax Error' is a problem detected when Python checks the code before it runs it. For more information, see the Python tutorial page on [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html).

# Booleans, Comparison Operators, and Logical Operators
The bool data type holds one of the values `True` or `False`, which are often encoded as `1` or `0`, respectively.

There are 6 comparison operators that are common to see in order to obtain a bool value:

| Symbol use case        | Bool          | Operation  |
| ------------- |:-------------:| -----:|
| 5 < 3      | False | Less than |
| 5 > 3      | False | Greater than |
| 3 <= 3      | True | Less than or Equal To |
| 3 >= 5      | False | Grater than or Equal To |
| 3 == 5      | False | Equal To |
| 3 != 5      | True | Not Equal To |

And there are three logical operators you need to be familiar with:

| Logical case        | Bool          | Operation  |
| ------------- |:-------------:| -----:|
| 5 < 3 `and` 5 == 5 | False | `and` Evaluates if all provided statements are true  |
| 5 < 3 `or` 5 == 5 | True | `or` Evaluates if at least one of many statements is True |
|`not` 5 < 3 | True | `not` Flips the bool value |

# Strings
Strings in Python are shown as the variable type `str`. You can define a string with either double quotes `"` or single quotes `'`. If the string you are creating actually has one of these two values in it, then you need to be careful to assure your code doesn't give an error.

```python
>>> my_string = 'this is a string!'
>>> my_string2 = "this is also a string!!!"
```

You can also include a `\` in your string to be able to include one of these quotes:

```python
>>> this_string = 'Simon\'s skateboard is in the garage.'
>>> print(this_string)
```

Output:
```python
Simon's skateboard is in the garage.
```

There are a number of other operations you can use with strings as well.

```python
>>> first_word = 'Hello'
>>> second_word = 'There'
>>> print(first_word + second_word)

HelloThere

>>> print(first_word + ' ' + second_word)

Hello There

>>> print(first_word * 5)

HelloHelloHelloHelloHello

>>> print(len(first_word))

5
```
Notice Python uses 0 indexing:

```python
>>> first_word[0]

H

>>> first_word[1]

e
```

**The len() function**
`len()` is a built-in Python function that returns the length of an object, like a string. The length of a string is the number of characters in the string. This will always be an integer.

# String Methods
In this video you were introduced to methods. Methods are like some of the functions you have already seen:

1. len("this")
2. type(12)
3. print("Hello world")
These three above are functions - notice they use parentheses, and accept one or more arguments. Functions will be studied in much more detail in a later lesson!

A **method** in Python behaves similarly to a function. Methods actually are functions that are called using dot notation. For example, `lower()` is a string method that can be used like this, on a string called "sample string": `sample_string.lower()`.

Methods are specific to the data type for a particular variable. So there are some built-in methods that are available for all strings, different methods that are available for all integers, etc.

```python
my_string = 'sebastian thrun'
>>> my_string.islower()
True
>>> my_string.count('a')
2
>>> my_string.find('a')
3
```

**One important string method: format()**
We will be using the `format()` string method a good bit in our future work in Python, and you will find it very valuable in your coding, especially with your print statements.

We can best illustrate how to use `format()` by looking at some examples:

```python
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
```

Output:
```python
Does your dog bite?
```
Example:

```python
maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))
```
Output:
```python
Maria loves math and statistics
```

You can learn more about strings and string methods by looking at the [string method documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).

**Another important string method: split()**
A helpful string method when working with strings is the `.split` method. This function or method returns a data container called a list that contains the words from the input string.

The `split` method has two additional arguments (*sep* and *maxsplit*). The *sep* argument stands for "separator". It can be used to identify how the string should be split up (e.g., whitespace characters like space, tab, return, newline; specific punctuation (e.g., comma, dashes)). If the sep argument is not provided, the default separator is whitespace.

True to its name, the *maxsplit* argument provides the maximum number of splits. The argument gives maxsplit + 1 number of elements in the new list, with the remaining string being returned as the last element in the list. You can read more about these methods in the Python documentation too.

Here are some examples for the `.split()` method.

1. A basic split method:

```python
new_str = "The cow jumped over the moon."
new_str.split()
['The', 'cow', 'jumped', 'over', 'the', 'moon.']
```
2. Here the separator is space, and the maxsplit argument is set to 3.
```python
new_str.split(' ', 3)
['The', 'cow', 'jumped', 'over the moon.']
```
3. Using '.' or period as a separator.
```python
new_str.split('.')
['The cow jumped over the moon', '']
```
4. Using no separators but having a maxsplit argument of 3.
```python
new_str.split(None, 3)
['The', 'cow', 'jumped', 'over the moon.']
```
