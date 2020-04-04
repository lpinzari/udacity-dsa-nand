# Lists

Data structures are containers that organize and group data types together in different ways. A list is one of the most common and basic data structures in Python.

You can create a list with square brackets. Lists can contain any mix and match of the data types you have seen so far.

```python
list_of_random_things = [1, 3.4, 'a string', True]
```

This is a list of 4 elements. All ordered containers (like lists) are indexed in python using a starting index of 0. Therefore, to pull the first value from the above list, we can write:

```python
>>> list_of_random_things[0]
1
```
You can retrieve the last element by reducing the index by 1. Therefore, you can do the following:

```python
>>> list_of_random_things[len(list_of_random_things) - 1]
True
```
Alternatively, you can index from the end of a list by using negative values, where -1 is the last element, -2 is the second to last element and so on.

```python
>>> list_of_random_things[-1]
True
>>> list_of_random_things[-2]
a string
```
## Slice and Dice with Lists

We can pull more than one value from a list at a time by using **slicing**. When using slicing, it is important to remember that the `lower index` is inclusive and the `upper index` is exclusive.

Therefore, this:

```python
>>> list_of_random_things = [1, 3.4, 'a string', True]
>>> list_of_random_things[1:2]
[3.4]
```
It will only return 3.4 in a list. Notice this is still different than just indexing a single element, because you get a list back with this indexing.The colon tells us to go from the starting value on the left of the colon up to, but not including, the element on the right.

If you know that you want to start at the beginning, of the list you can also leave out this value.

```python
>>> list_of_random_things[:2]
[1, 3.4]
```

or to return all of the elements to the end of the list, we can leave off a final element.

```python
>>> list_of_random_things[1:]
[3.4, 'a string', True]
```
This type of indexing works exactly the same on strings, where the returned value will be a string.

# Are you `in` or `not in` ?

We can also use **in** and **not in** to return a bool of whether an element exists within our list, or if one string is a substring of another.

```python
>>> 'this' in 'this is a string'
True
>>> 'in' in 'this is a string'
True
>>> 'isa' in 'this is a string'
False
>>> 5 not in [1, 2, 3, 4, 6]
True
>>> 5 in [1, 2, 3, 4, 6]
False
```
## Mutability and Order

**Mutability** is about whether or not we can change an object once it has been created. If an object (like a list or string) can be changed (**like a list can**), then it is called mutable. However, if an object **cannot be changed** with creating a completely new object (**like strings**), then the object is considered **immutable**.

```python
>>> my_lst = [1, 2, 3, 4, 5]
>>> my_lst[0] = 'one'
>>> print(my_lst)
['one', 2, 3, 4, 5]
```

As shown above, you are able to replace 1 with 'one' in the above list. This is because lists are **mutable**.

However, the following does not work:

```python
>>> greeting = "Hello there"
>>> greeting[0] = 'M'
```

This is because **strings are immutable**. This means to change this string, you will need to create a completely new string.

There are two things to keep in mind for each of the data types you are using:

- Are they **mutable**?
- Are they **ordered**?

**Order** is about whether the position of an element in the object can be used to access the element. **Both strings and lists are ordered**. We can use the order to access parts of a list and string.

However, you will see some data types in the next sections that will be unordered. For each of the upcoming data structures you see, it is useful to understand how you index, are they mutable, and are they ordered. Knowing this about the data structure is really useful!

Additionally, you will see how these each have different methods, so why you would use one data structure vs. another is largely dependent on these properties, and what you can easily do with it!

**Quiz Slicing**:

Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!

```python
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']


# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])
```

## Useful functions for lists I

- `len()` returns how many elements are in a list.
- `max()` returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number. The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically. This works because the the max function is defined in terms of the greater than comparison operator. The max function is undefined for lists that contain elements from different, incomparable types.
- `min()` returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.
- `sorted()` returns a copy of a list in order from smallest to largest, leaving the list unchanged.

## Useful Functions for Lists II

**join method**

Join is a **string method** that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.

```python
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
```

Output:

```python
fore
aft
starboard
port
```
In this example we use the string "\n" as the separator so that there is a newline between each element. We can also use other strings as separators with .join. Here we use a hyphen.

```python
name = "-".join(["García", "O'Kelly"])
print(name)
```

Output:

```python
García-O'Kelly
```
It is important to remember to separate each of the items in the list you are joining with a comma (,). Forgetting to do so will not trigger an error, but will also give you unexpected results.

**append method**

A helpful method called append adds an element to the end of a list.

```python
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
```
Output:

```python
['a', 'b', 'c', 'd', 'z']
```
