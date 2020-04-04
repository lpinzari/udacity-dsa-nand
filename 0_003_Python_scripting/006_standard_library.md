# The Standard Library

You've seen how helpful it could be to import your own modules. But what if I told you there is an entire library of built-in modules that just come with Python?
This is the Python Standard Library ([PSL](https://docs.python.org/3/library/)),[tutorial](https://pymotw.com/3/).
Using modules from the **PSL** to easily access and use existing code gives you a lot of programming power. The **PSL** is organized into modules. Many modules are simply Python files, like the Python scripts you've already written and imported. Modules typically contain a lot of definitions and usually don't show any output. Running the code make, all the module's functions and types of objects available to use.

## Quiz: Compute an Exponent
It's your turn to import and use the `math` module. Use the math module to calculate e to the power of 3. print the answer.

Refer to the math module's [documentation](https://docs.python.org/3.6/library/math.html?highlight=math%20module#module-math) to find the function you need!

```python
# print e to the power of 3 using the math module
import math

print(math.exp(3))
```

## Quiz: Password Generator
Write a function called `generate_password` that selects three random words from the list of `words word_list` and concatenates them into a single string. Your function should not accept any arguments and should reference the global variable `word_list` to build the password.

**words.txt**
```script
Alice
was
beginning
to
get
very
tired
of
sitting
by
her
```

**password_generator.py**
```python
# Use an import statement at the top
import random
word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces
n = len(word_list)
def generate_password():
    pssw = ''
    for i in range(1,4):
        pssw += word_list[random.randint(0,n-1)]
    return pssw



# test your function
print(generate_password())
```

## Our favourite modules
The Python Standard Library has a lot of modules! To help you get familiar with what's available, here are a selection of our favourite Python Standard Library modules and why we use them!

- [csv](https://docs.python.org/3/library/csv.html): very convenient for reading and writing csv files.
- [collections](https://docs.python.org/3/library/collections.html): useful extensions of the usual data types including `OrderedDict`, `defaultdict` and `namedtuple`.
- [random](https://docs.python.org/3/library/random.html): generates pseudo-random numbers, shuffles sequences randomly and chooses random items.
- [string](https://docs.python.org/3/library/string.html): more functions on strings. This module also contains useful collections of letters like `string.digits` (a string containing all characters which are valid digits).
- [re](https://docs.python.org/3/library/re.html): pattern-matching in strings via regular expressions.
- [math](https://docs.python.org/3/library/math.html): some standard mathematical functions.
- [os](https://docs.python.org/3/library/os.html): interacting with operating systems.
- [os.path](https://docs.python.org/3/library/os.path.html): submodule of `os` for manipulating path names.
- [sys](https://docs.python.org/3/library/sys.html): work directly with the Python interpreter.
- [json](https://docs.python.org/3/library/json.html): good for reading and writing json files (good for web work).

 
