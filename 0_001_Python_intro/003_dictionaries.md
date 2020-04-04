# Dictionaries and Identity Operators

A dictionary is a mutable data type that stores mappings of unique keys to values. Here's a dictionary that stores elements and their atomic numbers.

```python
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
```

Dictionaries can have keys of any **immutable type**, like integers, float or tuples, not just strings. *It's not even necessary for every key to have the same type!* We can look up values or insert new values in the dictionary using square brackets that enclose the key.

```python
print(elements["helium"])  # print the value mapped to "helium" i.e 1
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
```

We can check whether a value is **in** a dictionary the same way we check whether a value is in a list or set with the **in** keyword. Dicts have a related method that's also useful, get. **get** looks up values in a dictionary, but unlike square brackets, get returns *None* (or a *default value* of your choice) if the key isn't found.

```python
print("carbon" in elements)
print(elements.get("dilithium"))
```

This would output:

```python
True
None
```
Carbon is in the dictionary, so True is printed. Dilithium isn’t in our dictionary so None is returned by get and then printed. If you *expect* lookups to sometimes fail, **get** might be a better tool than normal square bracket lookups because errors can crash your program.

| keyword       | Operators         |
| ------------- | -------------:|
| is      | evaluates if both sides have same identity|
| is not      | evaluates if both sides have different identities     |

You can check if a key returned None with the **is** operator. You can check for the opposite using **is not**.

```python
n = elements.get("dilithium")
print(n is None)
print(n is not None)
```

This would output:

```python
True
False
```

## Quiz: Define a Dictionary
Define a dictionary named population that contains this data:

| keys       | values|
| ------------- | -------------:|
| Shanghai  | 17.8 |
| Instanbul | 13.3 |
| Karachi | 13.0|
| Mumbai | 12.5 |

```python
population = {'Shanghai': 17.8,
              'Istanbul': 13.3,
              'Karachi': 13.0,
              'Mumbai': 12.5}
```

What happens if we look up a value that isn't in the dictionary? Create a test dictionary and use the square brackets to look up a value that you haven't defined. What happens?

Answer: A **keyError** occurs.

## get with a Default Value
Dictionaries have a related method that's also useful, `get()`. `get()` looks up values in a dictionary, but unlike looking up values with square brackets, `get()` returns **None** (or a **default value of your choice**) if the key isn't found. If you expect lookups to sometimes fail, `get()` might be a better tool than normal square bracket lookups.

```python
>>> elements.get('dilithium')
None
>>> elements['dilithium']
KeyError: 'dilithium'
>>> elements.get('kryptonite', 'There\'s no such element!')
"There's no such element!"
```

In the last example we specified a default value (the string 'There's no such element!') to be returned instead of None when the key is not found.

## Checking for Equality vs. Identity: `==` vs. `is`

What will the output of the following code be?

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)
```

Answer: True, True, True, False

## Compound Data Structures
We can include containers in other containers to create compound data structures. For example, this dictionary maps keys to values that are also dictionaries!

```python
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
```

We can access elements in this nested dictionary like this.

```python
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
```

You can also add a new key to the element dictionary.

```python
oxygen = {"number":8,
          "weight":15.999,
          "symbol":"O"}  # create a new oxygen dictionary
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)
```

Output is:

```python
elements =  {"hydrogen": {"number": 1,
                          "weight": 1.00794,
                          "symbol": 'H'},
               "helium": {"number": 2,
                          "weight": 4.002602,
                          "symbol": "He"},
               "oxygen": {"number": 8,
                          "weight": 15.999,
                          "symbol": "O"}}
```

### Quiz: Adding Values to Nested Dictionaries
Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary. After inserting the new entries you should be able to perform these lookups:

```python
>>> print(elements['hydrogen']['is_noble_gas'])
False
>>> print(elements['helium']['is_noble_gas'])
True
```

```python
elements = {'hydrogen': {'number': 1,
                         'weight': 1.00794,
                         'symbol': 'H',
                         'is_noble_gas':False},
            'helium': {'number': 2,
                       'weight': 4.002602,
                       'symbol': 'He',
                       'is_noble_gas':True}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])
```
## Collections
When we have a group of data we can think about it as a collection (of data elements). In this lesson, we have seen many different data structures that Python provides for storing, accessing and manipulating collections of data. In particular, we have seen lists, sets, and dictionaries.

### Quiz: Count Unique Words
Your task for this quiz is to find the number of unique words in the text. In the code editor below, complete these three steps to get your answer.

1. Split verse into a list of words. Hint: You can use a string method you learned in the previous lesson.
2. Convert the list into a data structure that would keep only the unique elements from the list.
3. Print the length of the container.

```python
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, "\n")

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to set to get unique words
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique)
```

Output:

```python
if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise

['if', 'you', 'can', 'keep', 'your', 'head', 'when', 'all', 'about', 'you', 'are', 'losing', 'theirs', 'and', 'blaming', 'it', 'on', 'you', 'if', 'you', 'can', 'trust', 'yourself', 'when', 'all', 'men', 'doubt', 'you', 'but', 'make', 'allowance', 'for', 'their', 'doubting', 'too', 'if', 'you', 'can', 'wait', 'and', 'not', 'be', 'tired', 'by', 'waiting', 'or', 'being', 'lied', 'about', 'don’t', 'deal', 'in', 'lies', 'or', 'being', 'hated', 'don’t', 'give', 'way', 'to', 'hating', 'and', 'yet', 'don’t', 'look', 'too', 'good', 'nor', 'talk', 'too', 'wise']

{'or', 'when', 'hating', 'make', 'all', 'head', 'waiting', 'losing', 'don’t', 'to', 'look', 'about', 'yourself', 'by', 'wise', 'doubting', 'trust', 'deal', 'allowance', 'being', 'too', 'wait', 'in', 'nor', 'for', 'theirs', 'and', 'if', 'on', 'lied', 'are', 'your', 'but', 'give', 'yet', 'lies', 'good', 'men', 'tired', 'doubt', 'hated', 'blaming', 'can', 'be', 'keep', 'their', 'not', 'it', 'talk', 'way', 'you'}

51
```

Try to answer these using code, rather than inspecting the dictionary manually!

1. How many unique words are in verse_dict?
2. Is the key "breathe" in verse_dict?
3. What is the first element in the list created when verse_dict is sorted by keys?

Hint: Use the appropriate dictionary method to get a list of its keys, and then sort that list. Use this list of keys to answer the next two questions as well.
Which key (word) has the highest value in verse_dict?

```python
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1])
```
Output:

```python
{'make': 1, 'waiting': 1, 'tired': 1, 'when': 2, 'hating': 1, 'give': 1, 'talk': 1, 'losing': 1, 'look': 1, 'too': 3, 'doubting': 1, 'all': 2, 'be': 1, 'wait': 1, 'you': 6, 'it': 1, 'allowance': 1, 'being': 2, 'by': 1, 'for': 1, 'to': 1, 'men': 1, 'in': 1, 'can': 3, 'about': 2, 'are': 1, 'hated': 1, 'wise': 1, 'your': 1, 'yourself': 1, "don't": 3, 'good': 1, 'way': 1, 'keep': 1, 'if': 3, 'blaming': 1, 'nor': 1, 'but': 1, 'or': 2, 'on': 1, 'not': 1, 'deal': 1, 'trust': 1, 'doubt': 1, 'yet': 1, 'lied': 1, 'lies': 1, 'their': 1, 'theirs': 1, 'and': 3, 'head': 1}

51
False
about
yourself
```
