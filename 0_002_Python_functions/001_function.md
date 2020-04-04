# Defining Functions
Example of a function definition:

```python
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
```

After defining the cylinder_volume function, we **can** call the function like this.

```python
cylinder_volume(10, 3)
```

This is called a **function call statement**.

A function definition includes several important parts.

**Function Header**
Let's start with the function header, which is the first line of a function definition.

1. The function header always starts with the `def` keyword, which indicates that this is a function definition.
2. Then comes the function name (here, `cylinder_volume`), which follows the same naming conventions as variables.
3. Immediately after the name are parentheses that may include arguments separated by commas (here, `height` and `radius`). Arguments, or parameters, are values that are passed in as inputs when the function is called, and are used in the function body. If a function doesn't take arguments, these parentheses are left empty.
4. The header always end with a colon `:`.

**Function Body**

The rest of the function is contained in the body, which is where the function does its work.

1. The **body** of a function is the code indented after the header line. Here, it's the two lines that define `pi` and `return` the volume.
2. Within this body, we can refer to the **argument variables** and define new variables, which can only be used within these indented lines.
3. The body will often include a `return` statement, which is used to send back an **output value** from the function to the statement that called the function. A return statement consists of the `return` keyword followed by an expression that is evaluated to get the output value for the function. If there is no return statement, the function simply returns `None`.

**Naming Conventions for Functions**
Function names follow the same naming conventions as variables.

1. Only use ordinary letters, numbers and underscores in your function names. They can’t have spaces, and **need to start with a letter or underscore**.
2. You can’t use reserved words or built-in identifiers that have important purposes in Python. A list of Python reserved words is described [here](https://pentangle.net/python/handbook/node52.html).
3. Try to use descriptive names that can help readers understand what the function does.

**Default Arguments**
We can add default arguments in a function to have default values for parameters that are unspecified in a function call.

```python
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2
```

In the example above, `radius` is set to 5 if that parameter is omitted in a function call. If we call `cylinder_volume(10)`, the function will use 10 as the height and 5 as the radius. However, if we call `cylinder_volume(10, 7)` the 7 will simply overwrite the default value of 5.

Also notice here we are passing values to our arguments by position. It is possible to pass values in two ways - by **position** and by **name**. Each of these function calls are evaluated the same way.

```python
cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name
```

## Variable Scope
Variable scope refers to which parts of a program a variable can be referenced, or used, from.

It's important to consider **scope** when using variables in functions. If a variable is created inside a function, it can only be used within that function. Accessing it outside that function is not possible.

```python
# This will result in an error
def some_function():
    word = "hello"

print(word)
```

In the example above and the example below, `word` is said to have **scope** that is only **local** to each function. This means you can use the same name for different variables that are used in different functions.

```python
# This works fine
def some_function():
    word = "hello"

def another_function():
    word = "goodbye"
```

Variables defined outside functions, as in the example below, can still be accessed within a function. Here, word is said to have a **global scope**.

```python
# This works fine
word = "hello"

def some_function():
    print(word)

some_function()
```

Notice that we can still access the value of the global variable `word` within this function. However, the value of a global variable **can not be modified inside the function**. If you want to modify that variable's value inside this function, it should be passed in as an argument.

**More on Variable Scope**
When you program, you'll often find that similar ideas come up again and again. You'll use variables for things like counting, iterating and accumulating values to return. In order to write readable code, you'll find yourself wanting to use similar names for similar ideas. As soon as you put multiple piece of code together (for instance, multiple functions or function calls in a single script) you might find that you want to use the same name for two separate concepts.

Fortunately, you don't need to come up with new names endlessly. Reusing names for objects is OK as long as you keep them in separate scope.

**Good practice**: It is best to define variables in the smallest scope they will be needed in. While functions can refer to variables defined in a larger scope, this is very rarely a good idea since you may not know what variables you have defined if your program has a lot of variables.

QUIZ QUESTION
Read through this code snippet:

```python
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
```

Output: **An error occurs**

This code causes an **UnboundLocalError**, because the variable `egg_count` in the first line has global scope. Note that it is not passed as an argument into the function, so the function assumes the `egg_count` being referred to is the global variable.

You saw earlier that within a function, we can print a global variable's value successfully without an error. This worked because we were simply accessing the value of the variable. If we try to **change** or **reassign** this global variable, however, as we do in this code, we get an error. **Python doesn't allow functions to modify variables that aren't in the function's scope**.

A better way to write this would be:

```python
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
```
