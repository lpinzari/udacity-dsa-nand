# Lambda Expressions
You can use **lambda expressions** to create *anonymous functions*. That is, functions that don’t have a name. They are helpful for <u>creating quick functions that aren’t needed later in your code</u>. This can be especially useful for higher order functions, or functions that take in other functions as arguments.

With a lambda expression, this function:

```python
def multiply(x, y):
    return x * y
```

can be reduced to:

```python
multiply = lambda x, y: x * y
```

Both of these functions are used in the same way. In either case, we can call `multiply` like this:

```python
multiply(4, 7)
```

This returns 28.

**Components of a Lambda Function**
1. The `lambda` keyword is used to indicate that this is a lambda expression.
2. Following `lambda` are one or more arguments for the anonymous function separated by commas, followed by a colon :. Similar to functions, the way the arguments are named in a lambda expression is arbitrary.
3. Last is an expression that is evaluated and returned in this function. This is a lot like an expression you might see as a return statement in a function.

With this structure, lambda expressions aren’t ideal for complex functions, but can be very useful for short, simple functions.

## Quiz: Lambda with Map
`map()` is a higher-order built-in function that <u>takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable</u>. The code below uses `map()` to find the mean of each list in numbers to create the list averages.

Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to `map()`.

```python
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

#def mean(num_list):
 #   return sum(num_list) / len(num_list)
mean = lambda num_list: sum(num_list) / len(num_list)
averages = list(map(mean, numbers))
print(averages)
```
**Output**: `[57.0, 58.2, 50.6, 27.2]`

## Quiz: Lambda with Filter
`filter()` is a higher-order built-in function that <u>takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True</u>. The code below uses `filter()` to get the names in `cities` that are fewer than 10 characters long to create the list `short_cities`.

Rewrite this code to be more concise by replacing the `is_short` function with a lambda expression defined within the call to `filter()`.

```python
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)
```
**Output**: `['Chicago', 'Denver', 'Boston']`

### Additional Resources
If you want to learn more about writing functions, check out this [talk](https://www.youtube.com/watch?v=rrBJVMyD-Gs&feature=youtu.be) from PyCon by Jack Diederich. Diederich covers best practices for writing functions in Python that also apply to all code in Python.

Here's a great [blog](https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/) post about **yield** and **generators** from Jeff Knupp.
