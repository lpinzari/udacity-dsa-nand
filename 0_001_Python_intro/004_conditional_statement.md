# If Statement
An `if` statement is a conditional statement that runs or skips code based on whether a condition is true or false. Here's a simple example.

```python
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
```

Let's break this down.

1. An if statement starts with the `if` keyword, followed by the condition to be checked, in this case phone_balance < 5, and then a colon. The condition is specified in a boolean expression that evaluates to either True or False.

2. After this line is an indented block of code to be executed if that condition is true. Here, the lines that increment phone_balance and decrement bank_balance only execute if it is true that phone_balance is less than 5. If not, the code in this if block is simply skipped.

## If, Elif, Else
In addition to the if clause, there are two other optional clauses often used with an if statement. For example:

```python
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')
```

1. `if:` An if statement must always start with an if clause, which contains the first condition that is checked. If this evaluates to True, Python runs the code indented in this if block and then skips to the rest of the code after the if statement.

2. `elif:` elif is short for "else if." An elif clause is used to check for an additional condition if the conditions in the previous clauses in the if statement evaluate to False. As you can see in the example, you can have multiple elif blocks to handle different situations.

3. `else:` Last is the else clause, which must come at the end of an if statement if used. This clause doesn't require a condition. The code in an else block is run if all conditions above that in the if statement evaluate to False.

```python
state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)
```

## Indentation
Some other languages use braces to show where blocks of code begin and end. In Python we use indentation to enclose blocks of code. For example, if statements use indentation to tell Python what code is inside and outside of different clauses.

In Python, indents conventionally come in multiples of four spaces. Be strict about following this convention, because changing the indentation can completely change the meaning of the code. If you are working on a team of Python programmers, it's important that everyone follows the same indentation convention!

Spaces or Tabs?
The [Python Style Guide](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces) recommends using 4 spaces to indent, rather than using a tab. Whichever you use, be aware that "Python 3 disallows mixing the use of tabs and spaces for indentation."

## Complex Boolean Expressions
If statements sometimes use more complicated boolean expressions for their conditions. They may contain multiple comparisons operators, logical operators, and even calculations. Examples:

```python
if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")
```

For really complicated conditions you might need to combine some ands, ors and nots together. Use parentheses if you need to make the combinations clear.

However simple or complex, the condition in an if statement must be a boolean expression that evaluates to either True or False and it is this value that decides whether the indented block in an if statement executes or not.

### Good and Bad Examples
Here are some things to keep in mind while writing boolean expressions for your if statements.

1. **Don't use True or False as conditions**

```python
# Bad example
if True:
    print("This indented code will always get run.")
```
While "True" is a valid boolean expression, it's not useful as a condition since it always evaluates to True, so the indented code will always get run. Similarly, `if False` is not a condition you should use either - the statement following this if statement would never be executed.

```python
# Another bad example
if is_cold or not is_cold:
    print("This indented code will always get run.")
```
Similarly, it's useless to use any condition that you know will always evaluate to True, like this example above. A boolean variable can only be True or False, so either is_cold or not is_cold is always True, and the indented code will always be run.

2. **Be careful writing expressions that use logical operators**
Logical operators `and`, `or` and `not` have specific meanings that aren't quite the same as their meanings in plain English. Make sure your boolean expressions are being evaluated the way you expect them to.

```python
# Bad example
if weather == "snow" or "rain":
    print("Wear boots!")
```

This code is valid in Python, but it is not a boolean expression, although it reads like one. The reason is that the expression to the right of the `or` operator, **"rain"**, **is not a boolean expression - it's a string!** Later we'll discuss what happens when you use non-boolean-type objects in place of booleans.

3. **Don't compare a boolean variable with == True or == False**
This comparison isn’t necessary, since the boolean variable itself is a boolean expression.

```python
# Bad example
if is_cold == True:
    print("The weather is cold!")
```
This is a valid condition, but we can make the code more readable by using the variable itself as the condition instead, as below.

```python
# Good example
if is_cold:
    print("The weather is cold!")
```

If you want to check whether a boolean is False, you can use the `not` operator.

## Truth Value Testing
If we use a **non-boolean object as a condition** in an if statement in place of the boolean expression, Python will check for its truth value and use that to decide whether or not to run the indented code. By default, the truth value of an object in Python is considered True unless specified as False in the documentation.

Here are most of the built-in objects that are considered **False** in Python:

- constants defined to be false: `None` and `False`
- zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
- empty sequences and collections: `'""`, `()`, `[]`, `{}`, `set()`, `range(0)`
Example:

```python
errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")
```
In this code, **errors** has the truth value True because it's a non-zero number, so the error message is printed. This is a nice, succinct way of writing an if statement.
