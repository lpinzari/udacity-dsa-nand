# For Loops
Python has two kinds of loops - `for` loops and `while` loops. A for loop is used to **"iterate"**, or do something repeatedly, over an **iterable**.

An **iterable** is an object that can return one of its elements at a time. This can include **sequence types**, such as **strings**, **lists**, and **tuples**, as well as **non-sequence types**, such as **dictionaries** and **files**.

Example
Let's break down the components of a `for` loop, using this example with the list **cities**:

```python
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")
```

Components of a for Loop

1. The first line of the loop starts with the `for` keyword, which signals that this is a for loop
2. Following that is `city in cities`, indicating `city` is the iteration variable, and `cities` is the **iterable** being looped over. In the first iteration of the loop, city gets the value of the first element in `cities`, which is “new york city”.
3. The for loop heading line always ends with a colon `:`
4. Following the for loop heading is an indented block of code, the body of the loop, to be executed in each iteration of this loop. There is only one line in the body of this loop - print(city).
5. After the body of the loop has executed, we don't move on to the next line yet; we go back to the `for` heading line, where the iteration variable takes the value of the next element of the iterable. In the second iteration of the loop above, `city` takes the value of the next element in `cities`, which is "mountain view".
6. This process repeats until the loop has iterated through all the elements of the iterable. Then, we move on to the line that follows the body of the loop - in this case, print("Done!"). We can tell what the next line after the body of the loop is because it is unindented. Here is another reason why paying attention to your indentation is very important in Python!

Executing the code in the example above produces this output:

```python
new york city
mountain view
chicago
los angeles
Done!
```
### Naming convention
You can name iteration variables however you like. A common pattern is to give the iteration variable and iterable the same names, except the singular and plural versions respectively (e.g., 'city' and 'cities').

## Using the `range()` Function with `for` Loops:

`range()` is a built-in function used to create an **iterable sequence of numbers**. You will frequently use `range()` with a `for` loop to repeat an action a certain number of times. Any variable can be used to iterate through the numbers, but Python programmers conventionally use `i`, as in this example:

```python
for i in range(3):
    print("Hello!")
```

Output:

```python
Hello!
Hello!
Hello!
```

**range(start=0, stop, step=1)**

The `range()` function takes three integer arguments, the first and third of which are optional:

1. The 'start' argument is the first number of the sequence. If unspecified, 'start' defaults to 0.
2. The 'stop' argument is 1 more than the last number of the sequence. This argument must be specified.
3. The 'step' argument is the difference between each number in the sequence. If unspecified, 'step' defaults to 1.

Notes on using `range()`:

1. If you specify one integer inside the parentheses with `range()`, it's used as the value for 'stop,' and the defaults are used for the other two.
**e.g.** - `range(4)` returns `0, 1, 2, 3`.

2. If you specify two integers inside the parentheses with `range()`, they're used for 'start' and 'stop,' and the default is used for 'step.'
**e.g.** - `range(2, 6)` returns `2, 3, 4, 5`.

3. Or you can specify all three integers for 'start', 'stop', and 'step.'
**e.g.** - `range(1, 10, 2)` returns `1, 3, 5, 7, 9`.

### Creating and Modifying Lists
In addition to extracting information from lists, as we did in the first example above, you can also create and modify lists with for loops. You can create a list by appending to a new list at each iteration of the for loop like this:


```python
# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
```

**Modifying** a list is a bit more involved, and requires the use of the `range()` function.

We can use the `range()` function to generate the indices for each value in the `cities` list. This lets us access the elements of the list with `cities[index]` so that we can **modify the values in the cities list in place**.

```python
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()
```

Quiz:
Use a for loop to take a list and print each element of the list in its own line.

```python
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for word in sentence:
    print(word)
```
Output:

```python
the
quick
brown
fox
jumped
over
the
lazy
dog
```

Solution: Multiples of 5
Here is our solution for this one:

```python
for i in range(5, 35, 5):
    print(i)
```

Output:

```python
5
10
15
20
25
30
```

### Quiz: Create Usernames
Write a `for` loop that iterates over the `names` list to create a `usernames` list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your `for` loop over the list:

```python
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)
```

Output:

```python
['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']
```

### Quiz: Modify Usernames with Range
Write a for loop that uses `range()` to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores.

```python
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)
```

Output:

```python
['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']
```

### Quiz: Tag Counter
Write a `for` loop that iterates over a list of strings, `tokens`, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable `count`.

You can assume that the list of strings will not contain empty strings.
You can use string indexing to find out if each token begins and ends with angle brackets.

```python
tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)
```

Output: `2`

### Quiz: Create an HTML List
Write some code, including a `for` loop, that iterates over a list of strings and creates a single string, `html_str`, which is an HTML list. For example, if the list is `items = ['first string', 'second string']`, printing html_str should output:

```python
<ul>
<li>first string</li>
<li>second string</li>
</ul>
```

That is, the string's first line should be the opening tag `<ul>`. Following that is one line per element in the source list, surrounded by `<li>` and `</li>` tags. The final line of the string should be the closing tag `</ul>`.

```python
items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)
```

Output:

```python
<ul>
<li>first string</li>
<li>second string</li>
</ul>
```

Example:

| INPUT       | OUTPUT|
| ------------- | -------------:|
| print(list(range(4)))  | [0, 1, 2, 3] |
| print(list(range(4,8))) | [4, 5, 6, 7] |
| print(list(range(4,10,2))) | [4, 6, 8]|
| print(list(range(0,-5))) | [] |
