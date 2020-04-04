# Quantifying efficiency
It's fine to say "this algorithm is more efficient than that algorithm", but can we be more specific than that? Can we quantify things and say how much more efficient the algorithm is?

Let's look at a simple example, so that we have something specific to consider.

Here is a short (and rather silly) function written in Python:

```python
def some_function(n):
    for i in range(2):
        n += 100
    return n
```
##### Quiz 1
What does it do?
Answer: `Adds 200 to the given input`

Now how about this one?

##### Quiz 2

```python
def other_function(n):
    for i in range(100):
        n += 2
    return n
```
Answer: `Adds 200 to the given input`

##### Quiz 3
So these functions have exactly the same end result. But can you guess which one is more efficient?

Here they are next to each other for comparison:

```python
def some_function(n):
    for i in range(2):
        n += 100
    return n

def other_function(n):
    for i in range(100):
        n += 2
    return n
```

Answer: `some_function` is more efficient.

Although the two functions have the exact same end result, one of them iterates many times to get to that result, while the other iterates only a couple of times.

This was admittedly a rather impractical example (you could skip the `for` loop altogether and just add `200` to the input), but it nevertheless demonstrates one way in which efficiency can come up.

## Counting lines
With the above examples, what we basically did was count the number of lines of code that were executed. Let's look again at the first function:

```python
def some_function(n):
    for i in range(2):
        n += 100
    return n
```

There are four lines in total, but the line inside the `for` loop will get run twice. So running this code will involve running 5 lines.

Now let's look at the second example:

```python
def other_function(n):
    for i in range(100):
        n += 2
    return n
```

In this case, the code inside the loop runs 100 times. So running this code will involve running 103 lines!

Counting lines of code is not a perfect way to quantify efficiency, and we'll see that there's a lot more to it as we go through the program. But in this case, it's an easy way for us to approximate the difference in efficiency between the two solutions. We can see that if Python has to perform an addition operation 100 times, this will certainly take longer than if it only has to perform an addition operation twice!
