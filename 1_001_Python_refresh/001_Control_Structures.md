# Control Structures

## Iteration with Loops
To iterate in Python, there are several options. A <button>for</button> loop can be used to iterate through a list or dictionary. Instead of the traditional for loop where we initialize a value <button>i</button> and **increase / decrease** it till it reaches an end value, Python's for loops are <button>for-each</button> in nature. This means that when you are iterating using a for loop over a list, you actually **iterate over the items of that list.**

If you also need the index values from the list while iterating, another possibility is to use <button>enumerate</button>, which is shown in an example below.

An additional way to iterate in Python is with a <button>while</button> loop. Just as in other programming languages, the while loop will repeat while some conditional statement is true. You will see more on conditional statements shortly, but first, here are examples of iteration with for and while loops.

```python
# Examples of iteration with for loops.

my_list = [0, 1, 2, 3, 4, 5]

# Print each value in my_list. Note you can use the "in" keyword to iterate over a list.
for item in my_list:
    print('The value of item is: ' + str(item))

# Print each index and value pair.
for i, value in enumerate(my_list):
    print('The index value is: ' + str(i) + '. The value at i is: ' + str(value))

# Print each number from 0 to 9 using a while loop.
i = 0
while(i < 10):
    print(i)
    i += 1

# Print each key and dictionary value. Note that you can use the "in" keyword
# to iterate over dictionary keys.
my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
for key in my_dict:
    print(key + ', ' + my_dict[key])
```

Remember that Python requires correct indentation for code blocks to be interpreted correctly. Indentation for a block is usually four spaces, or one tab length.

#### QUESTION 1 OF 3

What would be the output of the following code?

```Python
my_dict = {'a':[0, 1, 2, 3], 'b':[0, 1, 2, 3], 'c':[0, 1, 2, 3], 'd':[0, 1, 2, 3]}
i = 0
output = []
for key in my_dict:
    output.append(my_dict[key][i])
    i += 1
print(output)
```
Answer: `[0, 1, 2, 3]`

## Conditional Statements
Conditional statements use boolean logic to help guide our decision process: the statement is true or false. These statements are structured using comparison operators: greater than <button>(>)</button>, less than <button>(<)</button>, and equal to <button>(==)</button>.

Using conditional statements for control flow is accomplished in Python with the keywords: <button>if</button>, <button>else</button>, and <button>elif</button>. When doing multiple comparisons in Python, one after the other, the first comparison always uses <button>if</button> and the last comparison generally uses <button>else</button>. If additional control flow is needed, elif statements can be used; elif stands for "else if".

```Python
num = 5
if num < 5:
    print('The number is smaller than 5.')
elif num == 5:
    print('The number equals 5.')
else:
    print('The number is greater than 5.')
```
Answer: `the number equals 5`

### Control Structure Practice
In the following exercise you will finish writing `smallest_positive` which is a function that finds the smallest positive number in a list.

```python
def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_pos = None
    for num in in_list:
        if num > 0:
            # Note: we use a logical "or" in this solution to form
            # the conditional statement, although this was
            # not introduced above.
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None
```
