# Space Complexity Examples
When we refer to space complexity, we are talking about how efficient our algorithm is in terms of **memory usage**. This comes down to the datatypes of the variables we are using and their allocated space requirements. In Python, it's less clear how to do this due to the underlying data structures using more memory for house keeping functions (as the language is actually written in C).

For example, in C/C++, an integer type takes up 4 bytes of memory to store the value, but in Python 3 an integer takes 14 bytes of space. Again, this extra space is used for housekeeping functions in the Python language.

For the examples of this lesson we will avoid this complexity and assume the following sizes:

| Type | Storage size |
| ------------- |-------------:|
| char    | 1 byte |
| bool    | 1 byte |
| int | 4 byte |
| float | 4 byte |
| double | 8 byte |


It is also important to note that we will be focusing on just the data space being used and not any of the environment or instructional space.

### Example 1

```python
def our_constant_function():

    x = 3 # Type int
    y = 345 # Type int
    z = 11 # Type int

    answer = x+y+z

    return answer
```

So in this example we have four integers `(x, y, z and answer)` and therefore our space complexity will be `4*4 = 16 bytes`. This is an example of **constant space complexity**, since the amount of space used does not change with input size.


### Example 2

```python

def our_linear_function(n):

    n = n # Type int
    counter = 0 # Type int
    list_ = [] # Assume that the list is empty (i.e., ignore the fact that there is actually meta data stored with Python lists)

    while counter < n:
        list_.append(counter)
        counter = counter + 1

    return list_
```

So in this example we have two integers `(n and counter)` and an **expanding list**, and therefore our space complexity will be **4*n + 8** since we have an **expanding integer list** and two integer data types. This is an example of **linear space complexity**.
