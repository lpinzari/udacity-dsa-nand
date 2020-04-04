# Zip and Enumerate
`zip` and `enumerate` are useful built-in functions that can come in handy when dealing with loops.

## Zip
`zip` returns an **iterator** that **combines multiple iterables into one sequence of tuples**. Each tuple <u>contains the elements in that position</u> from all the iterables. For example, printing

`list(zip(['a', 'b', 'c'],[1, 2, 3]))`

would output: `[('a', 1), ('b', 2), ('c', 3)]`.

Like we did for `range()` **we need to convert it to a list** or iterate through it with a loop to see the elements.

You could **unpack each tuple** in a `for` loop like this.

```python
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
```
In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.

```python
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
```

This would create the same `letters` and `nums` tuples we saw earlier.

## Enumerate
`enumerate` is a built in function that returns an **iterator of tuples containing indices and values of a list**. You'll often use this when <u>you want the index along with each element of an iterable in a loop</u>.

```python
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
```

This code would output:

```python
0 a
1 b
2 c
3 d
4 e
```

### Quiz: Zip Coordinates Label
Use `zip` to write a `for` loop that creates a string specifying the label and coordinates of each point and appends it to the list `points`. Each string should be formatted as `label: x, y, z`. For example, the string for the first coordinate should be `F: 23, 677, 4`.

```python
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)
```

Output:

```python
F: 23, 677, 4
J: 53, 233, 16
A: 2, 405, -6
Q: -12, 433, -42
Y: 95, 905, 3
B: 103, 376, -6
W: 14, 432, 23
X: -5, 445, -1
```

Notice here, the tuple was unpacked using `*` in the `format` method. This can help make your code cleaner!

### Quiz: Zip Lists to a Dictionary
Use `zip` to create a dictionary `cast` that uses `names` as keys and `heights` as values.

```python
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)
```

Output:
The order of elements in this output may vary since dictionaries are unordered.

```python
{'Lily': 66, 'Barney': 72, 'Marshall': 76, 'Ted': 72, 'Robin': 68}
```

### Quiz: Unzip Tuples
Unzip the cast tuple into two `names` and `heights` tuples.

```python
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)
print(names)
print(heights)
```

Output:

```python
('Barney', 'Robin', 'Ted', 'Lily', 'Marshall')
(72, 68, 72, 66, 76)
```

### Quiz: Transpose with Zip
Use `zip` to transpose data from a **4-by-3 matrix** to a **3-by-4 matrix**.

```python
data = ((0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)
```

Output:

```python
((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))
```

### Quiz: Enumerate
Use `enumerate` to modify the `cast` list so that each element contains the name followed by the character's corresponding height. For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".

```python
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)
```

Output:

```python
['Barney Stinson 72', 'Robin Scherbatsky 68', 'Ted Mosby 72', 'Lily Aldrin 66', 'Marshall Eriksen 76']
```
