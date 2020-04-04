# Big O Notation
When describing the efficiency of an algorithm, we could say something like "the run-time of the algorithm increases linearly with the input size". This can get wordy and it also lacks precision. So as an alternative, mathematicians developed a form of notation called **big O notation**.

The **"O"** in the name refers to the order of the function or algorithm in question. And that makes sense, because big O notation is used to describe the **order**—or **rate of increase** — *in the run-time* of an algorithm, in terms of the *input size (n)*.

#### Quiz 1:

When you see some Big O notation, such as O(2n + 2), what does n refer to?

Answer: The length of the input to your algorithm.

Here's the cipher pseudocode:

```python
function decode(input):
    create output string
    for each letter in input:
        get new_letter from letter's location in cipher
        add new_letter to output
    return output
```

The estimated efficiency is O(2n + 2). Suppose the input string is "jzqh". What is n in this case?

Answer: 4


#### Quiz 2:
Which of these is the same as O(1)?

Answer: **O(0*n + 1)**

Here's one of the functions we looked at on the last page:

```python
def say_hello(n):
    for i in range(n):
        print("Hello!")
```

Which of these would best approximate the efficiency using big O notation?

Answer: `n`

#### Quiz 3:

```python
def say_hello(n):
    for i in range(n):
        for i in range(n):
            print("Hello!")
```

Answer: n<sup>2</sup>


In the examples we've looked at here, we've been approximating efficiency by counting the number of lines of code that get executed. But when we are thinking about the run-time of a program, what we really care about is how fast the computer's processor is, and how many operations we're asking the processor to perform. Different lines of code may demand very different numbers of operations from the computer's processor. For now, counting lines will work OK as an approximation, but as we go through the course you'll see that there's a lot more going on under the surface.
