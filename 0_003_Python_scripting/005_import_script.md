# Importing Local Scripts
We can actually import Python code from other scripts, which is helpful if you are working on a bigger project where you want to organize your code into multiple files and reuse code in those files. If the Python script you want to import is in the same directory as your current script, you just type import followed by the name of the file, without the .py extension.

**demo.py**
```python
import other_script
print(4)
```

**other_script.py**
```python
print(2+3)
```

You're only able to access what you've imported after the import statement. So, it's just less confusing to have this written first. It is also nice for the reader to see what a script depends on before reading the rest of the code.

```script
$ python demo.py
5
4
```
When we run `demo.py`, the import statement tells Python to run code from the `other_script.py` file which prints 5. It then continues to execute the rest of the code in this file and printing 4. If instead we have:

**other_script.py**
```python
num = 2 + 3
```
And we try to access the variable `num` in the `demo.py`, like this:

**demo.py**
```python
import other_script
print(num)
```

```script
$ python demo.py
Traceback (most recent call last):
  File "demo.py", line 2, in <module>
  print(num)
NameError: name 'num' is not defined
```

Referencing the variable `num` with just the name of the variable would return an error. To access objects in `other_script.py`, we need to use the name of the file followed by a dot followed by the object to tell Python to look for this object in the `other_script.py` file we imported.

**demo.py**
```python
import other_script
print(other_script.num)
```

When Python runs the script, it only has direct access to objects defined in the script. One of these objects is a **module** called `other_script`. A **module** is just a file with Python definitions and statements. When we import a Python file, it creates an object called `other_script` with a type **module**. Let's see a more useful example:

**useful_functions.py**
```python
def mean(num_list):
  return sum(num_list)/len(num_list)

def add_five(num_list):
  return [n+5 for n in num_list]
```

**demo.py**
```python
import useful_functions

scores = [88, 92, 79, 93, 85]
mean = useful_functions.mean(scores)
curved = useful_functions.add_five(scores)

mean_c = useful_functions.mean(curved)
print("Scores:", scores)
print("Original Mean:", mean, "New Mean:", mean_c)
```

Output:
```script
$ python demo.py
Scores: [88, 92, 79, 93, 85]
Original Mean: 87.4 New Mean: 92.4
```

Although it is a little bit annoying to type out the whole name of the file each time we want to use a function from it. We can make this much simpler by adding an **alias**.

**demo.py**
```python
import useful_functions as uf

scores = [88, 92, 79, 93, 85]
mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)
print("Scores:", scores)
print("Original Mean:", mean, "New Mean:", mean_c)
```

This is useful when we have objects we want to import from other Python scripts like functions. But, what if that script also includes executable statements in addition to function definitions that we don't want to import.

**useful_functions.py**
```python
def mean(num_list):
  return sum(num_list)/len(num_list)

def add_five(num_list):
  return [n+5 for n in num_list]

print("Testing mean function")
n_list = [34, 44, 23, 46, 12, 24]
correct_mean = 30.5
assert(mean(n_list) == correct_mean)

print("Testing add_five function")
correct_list = [39, 49, 28, 51, 17, 29]
assert(add_five(n_list) == correct_list)

print("All tests passed!")
```

For example, what if `useful_functions.py` has code at the bottom of the script that tests its functions and prints the results ?

```script
$ python useful_functions.py
Testing mean function
Testing add_five function
All tests passed!
```

This code is nice if we run `useful_functions.py` to test out these functions.

```script
$ python demo.py
Testing mean function
Testing add_five function
All tests passed!
Scores: [88, 92, 79, 93, 85]
Original Mean: 87.4 New Mean: 92.4
```
But unnecessary if we're just trying to use these functions in another script.

## Using a main block
To avoid running executable statements in a script when it's imported as a module in another script, include these lines in an  ` if __name__ == "__main__"` block. Or alternatively, include them in a function called `main()` and call this in the `if main` block.

**useful_functions.py**
```python

def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()
```

**demo.py**
```python
import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)
```

```script
$ python useful_functions.py
Testing mean function
Testing add_five function
All tests passed!
```

```script
$ python demo.py
Scores: [88, 92, 79, 93, 85]
Original Mean: 87.4 New Mean: 92.4
__main__
useful_functions
```

By including the executable statements in the `main()` function and calling the function in the `if __name__ == '__main__' ` block, we tell Python to execute the code only when the main program being executed is `useful_functions.py`. However, if we run another script that simply imports useful_function.py, the code is not run.

Whenever we run a script like this, Python actually sets a special built-in variable called `__name__` for any module. When we run a script, Python recognizes this module as the main program, and sets the `__name__` variable for this module to the string "**__main__**". For any modules that are imported in this script, this built-in `__name__` variable is just set to the name of that module. Therefore, the condition if `__name__ == "__main__"` is just checking whether this module is the main program.
