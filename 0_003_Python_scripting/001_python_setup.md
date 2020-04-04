# Is Python Already Installed On Your Computer?

Open up your Terminal or Command Line (this would be Git Bash on Windows).

In a new terminal or command prompt, type:
```python
$ python --version
```

and press `return`

You might get a response that the Python version installed is something like `Python 2.7.9`. In that case, it would tell you that you have Python 2 installed.

If instead the version number starts with a 3, then you already have Python 3 installed! Don't install Python again!

Alternatively, you might see an error message.

## Install Python using Anaconda

If you are interested in learning Python for data science, we strongly recommend installing [Anaconda](https://www.anaconda.com/distribution/), even if you already have Python installed on your computer.

Anaconda includes a great distribution of libraries and software built for data science, some of which are otherwise difficult to install. It also makes it really easy to [set up different environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) on your computer so you can quickly switch between different versions of Python and packages! For example, if one project you're working on requires Python 2.7 and another requires Python 3.6, as well as different dependencies, then Anaconda's environment management can help.

If you would like to know more about the Anaconda environment, you can check out the free course [here](https://classroom.udacity.com/courses/ud1111).

To test if you can now run Anaconda, enter `conda --version` in your terminal. This should print the version number of your installation. However, if you get a command not found message, you probably need to add Anaconda and Python to your PATH.

## Run a Python Script!

1. Open your terminal and use cd to navigate to the directory containing that python file script.py.
2. Now that you’re in the directory with the file, you can run it by typing `python script.py` and pressing enter.

## Scripting With Raw Input
We can get raw input from the user with the built-in function `input`, which takes in an optional string argument that you can use to specify a message to show to the user when asking for input.

```python
name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))
```

This prompts the user to enter a name and then uses the `input` in a greeting. The input function takes in whatever the user types and stores it as a string. If you want to interpret their input as something other than a string, like an integer, as in the example below, you need to wrap the result with the new type to convert it from a string.

```python
num = int(input("Enter an integer"))
print("hello" * num)
```

We can also interpret user input as a Python expression using the built-in function `eval`. This function evaluates a string as a line of Python.

```python
result = eval(input("Enter an expression: "))
print(result)
```
If the user inputs `2 * 3`, this outputs `6`.
