# Errors And Exceptions
- **Syntax** errors occur when Python can’t interpret our code, since we didn’t follow the correct syntax for Python. These are errors you’re likely to get when you make a typo, or you’re first starting to learn Python.

- **Exceptions** occur when unexpected things happen during execution of a program, even if the code is syntactically correct. There are different types of built-in exceptions in Python, and you can see which exception is thrown in the error message.

In Python there are ways to handle exceptions, so they don't always crush program when they occur. Let's look an example:

**demo.py**
```python
x = int(input('Enter a number:'))
```

*run the script*:
```console
$ python demo.py
Enter a number: nope
Traceback (most recent call last):
  File "demo.py", line 1, in <module>
  x = int(input('Enter a number:'))
ValueError: invalid literal for int() with base 10: 'nope'  
```
We go an error when the user inputs something that can't be converted to an int. We can actually handle this error using a `try` statement.

In a `try` statement, the code inside the `try` block is first run and if Python <u>runs into any exceptions</u> while it's running this block, it will jump to the code in the except block and moves on the rest of the code.

**demo.py**
```python
try:
  x = int(input('Enter a number:'))
except:
  print('That\`s not a valid number!')
print('\n Attempted Input\n')
```
*run the script*:
```console
$ python demo.py
Enter a number: ten
That`s not a valid number

Attempted Input

$ python demo.py
Enter a number: 10

Attempted Input
```
If we want this code keep running until the user inputs a valid number, we can use the `while` loop and `break` the loop if all the code in the try block successfully executes.

**demo.py**
```python
while True:
  try:
    x = int(input('Enter a number:'))
    break
  except:
    print('That\`s not a valid number!')
  print('\n Attempted Input\n')
```

*run the script*:

```console
$ python demo.py
Enter a number: ten
That`s not a valid number

Attempted Input

Enter a number: 10
```

If I enter a valid number the first statement in the try block doesn't raise an exception. So it moves on to the next line where it breaks from the loop. However, since it breaks from the loop it never prints `Attempted Input`. If we want the last line to always run after the try statement no matter what, there is an optional components of the statement we can use. The `finally` block.

**demo.py**
```python
while True:
  try:
    x = int(input('Enter a number:'))
    break
  except:
    print('That\`s not a valid number!')
  finally:
    print('\n Attempted Input\n')
```
run the script:

```console
$ python demo.py
Enter a number: ten
That`s not a valid number

Attempted Input

$ python demo.py
Enter a number: 10

Attempted Input
```

The `finally` block is useful for cleaning up actions in your code. For example, closing a file after attempting to open one in a try statement.

## Recap:

Try Statement
We can use try statements to handle exceptions. There are four clauses you can use.

1. `try`: This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
2. `except`: If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
3. `else`: If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
4. `finally`: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.


**Why do we need the `finally` clause in Python ?** [link](https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python)

In the previous example, the `except` block occurs when any kind of exception occurs while executing the `try` block. Really though we just want to adjust the **ValueError** exception. If I try to exit the program with Control+C `^C`, it doesn't stop the program because the except handles any error, including the **KeyboardInterrupt** error.

```console
$ python demo.py
Enter a number:^CThat`s not a valid number

Attempted Input

Enter a number: 10

Attempted Input
```

We can actually specify which error we want to handle like this:

**demo.py**
```python
while True:
  try:
    x = int(input('Enter a number:'))
    break
  except ValueError:
    print('That\`s not a valid number!')
  finally:
    print('\n Attempted Input\n')
```

Now it catches the **ValueError** exception, but not other exceptions like the **KeyboardInterrupt**.

*run the script*:
```console
$ python demo.py
Enter a number: ^C
Attempted Input
Traceback (most recent call last):
  File "demo.py", line 1, in <module>
  x = int(input('Enter a number:'))
KeyboardInterrupt
$  
```
Notice, in this case when you press `^C` it ends the program. This is because a **KeyboardInterrupt** exception was raised, which isn't handled by the `try` statement. Also notice that although the program crashed, the code in the `finally` block is still executed. `Attempted Input` is printed no matter what as the program is exiting the `try` statement, even if that means exiting the program. If we want the *handler* to address more than one type of exception, we can include a tuple after the `except` with the exception name, like this: `except ValueError, KeyboardInterrupt:`. Alternatively, if we want to execute different blocks of code depending on the exception, you can have multiple except blocks like this:

**demo.py**
```python
while True:
  try:
    x = int(input('Enter a number:'))
    break
  except ValueError:
    print('That\`s not a valid number!')
  except KeyboardInterrupt:
    print('\nNo Input taken')
    break
  finally:
    print('\n Attempted Input\n')
```

Now when we press `^C`, it says `No Input taken` and breaks from the while loop.

## Specifying Exceptions Recap
We can actually specify which error we want to handle in an except block like this:

```python
try:
    # some code
except ValueError:
    # some code
```

Now, it catches the `ValueError` exception, but not other exceptions. If we want this handler to address more than one type of exception, we can include a parenthesized tuple after the `except` with the exceptions.

```python
try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code
```

Or, if we want to execute different blocks of code depending on the exception, you can have multiple `except` blocks.

```python
try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code
```

## Accessing Error Messages
When you handle an exception, you can still access its error message like this:

```python
try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))
```

This would print something like this:

```python
ZeroDivisionError occurred: integer division or modulo by zero
```
So you can still access error messages, even if you handle them to keep your program from crashing!

If you don't have a specific error you're handling, you can still access the message like this:

```python
try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))
```

Exception is just the base class for all built-in exceptions. You can learn more about Python's exceptions [here](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).
