# Tuples

A tuple is another useful container. It's a data type for **immutable ordered sequences of elements**. They are often used to store **related pieces of information**. Consider this example involving latitude and longitude:

```python
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])
```

Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indices. Unlike lists, however, tuples are immutable - you can't add and remove items from tuples, or sort them in place.

Tuples can also be used to assign multiple variables in a compact way.

```python
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))
```

The parentheses are optional when defining tuples, and programmers frequently omit them if parentheses don't clarify the code.

In the second line, three variables are assigned from the content of the tuple dimensions. This is called tuple unpacking. You can use tuple unpacking to assign the information from a tuple into multiple variables without having to access them one by one and make multiple assignment statements.

If we won't need to use dimensions directly, we could shorten those two lines of code into a single line that assigns three variables in one go!

```python
length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))
```

# Sets

A set is a data type for mutable unordered collections of unique elements.One application of a set is to quickly remove duplicates from a list.

```python
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)
```

This would output:

```python
{1, 2, 3, 6}
```

Sets support the in operator the same as lists do. You can `add` elements to sets using the add method, and remove elements using the `pop` method, similar to lists. Although, when you pop an element from a set, a random element is removed. Remember that sets, unlike lists, are *unordered* so there is no "last element".

```python
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)
```

This outputs:

```python
False
{'grapefruit', 'orange', 'watermelon', 'banana', 'apple'}
grapefruit
{'orange', 'watermelon', 'banana', 'apple'}
```

Other operations you can perform with sets include those of mathematical sets. Methods like union, intersection, and difference are easy to perform with sets, and are much faster than such operators with other containers.
