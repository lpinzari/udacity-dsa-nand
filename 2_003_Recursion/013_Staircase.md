
### Problem Statement

Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. In how many possible ways can you climb the staircase if the staircase has `n` steps? Write a recursive function to solve the problem.

**Example:**

* `n = 3`
* `output = 4`
    
The output is `4` because there are four ways we can climb the staircase:
    
    1. 1 step +  1 step + 1 step
    2. 1 step + 2 steps 
    3. 2 steps + 1 step
    4. 3 steps


```python
def staircase(n):
    """
    :param: n - number of steps in the staircase
    Return number of possible ways in which you can climb the staircase
    TODO - write a recursive function to solve this problem
    """
    pass
```

<span class="graffiti-highlight graffiti-id_w7lklez-id_brqvnra"><i></i><button>Hide Solution</button></span>


```python
# Solution
## Read input as specified in the question.
## Print output as specified in the question.


def staircase(n):
    print('---- staircase({}) ---- START'.format(n))
    if n <= 0:
        print('Base case: 1')
        print('---- staircase({}) ---- END'.format(n))
        return 1
    
    if n == 1:
        print('Base case: 1')
        print('---- staircase({}) ---- END'.format(n))
        return 1
    elif n == 2:
        print('Base case: 2')
        print('---- staircase({}) ---- END'.format(n))
        return 2
    elif n == 3:
        print('Base case: 4')
        print('---- staircase({}) ---- END'.format(n))
        return 4
    output = staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
    print('output: {}'.format(output))
    print('---- staircase({}) ---- END'.format(n))
    return output
```


```python
def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
```


```python
n = 3
solution = 4
test_case = [n, solution]
test_function(test_case)
```

    ---- staircase(3) ---- START
    Base case: 4
    ---- staircase(3) ---- END
    Pass



```python
n = 4
solution = 7
test_case = [n, solution]
test_function(test_case)
```

    ---- staircase(4) ---- START
    ---- staircase(3) ---- START
    Base case: 4
    ---- staircase(3) ---- END
    ---- staircase(2) ---- START
    Base case: 2
    ---- staircase(2) ---- END
    ---- staircase(1) ---- START
    Base case: 1
    ---- staircase(1) ---- END
    output: 7
    ---- staircase(4) ---- END
    Pass



```python
n = 7
solution = 44
test_case = [n, solution]
test_function(test_case)
```

    ---- staircase(7) ---- START
    ---- staircase(6) ---- START
    ---- staircase(5) ---- START
    ---- staircase(4) ---- START
    ---- staircase(3) ---- START
    Base case: 4
    ---- staircase(3) ---- END
    ---- staircase(2) ---- START
    Base case: 2
    ---- staircase(2) ---- END
    ---- staircase(1) ---- START
    Base case: 1
    ---- staircase(1) ---- END
    output: 7
    ---- staircase(4) ---- END
    ---- staircase(3) ---- START
    Base case: 4
    ---- staircase(3) ---- END
    ---- staircase(2) ---- START
    Base case: 2
    ---- staircase(2) ---- END
    output: 13
    ---- staircase(5) ---- END
    ---- staircase(4) ---- START
    ---- staircase(3) ---- START
    Base case: 4
    ---- staircase(3) ---- END
    ---- staircase(2) ---- START
    Base case: 2
    ---- staircase(2) ---- END
    ---- staircase(1) ---- START
    Base case: 1
    ---- staircase(1) ---- END
    output: 7
    ---- staircase(4) ---- END
    ---- staircase(3) ---- START
    Base case: 4
    ---- staircase(3) ---- END
    output: 24
    ---- staircase(6) ---- END
    ---- staircase(5) ---- START
    ---- staircase(4) ---- START
    ---- staircase(3) ---- START
    Base case: 4
    ---- staircase(3) ---- END
    ---- staircase(2) ---- START
    Base case: 2
    ---- staircase(2) ---- END
    ---- staircase(1) ---- START
    Base case: 1
    ---- staircase(1) ---- END
    output: 7
    ---- staircase(4) ---- END
    ---- staircase(3) ---- START
    Base case: 4
    ---- staircase(3) ---- END
    ---- staircase(2) ---- START
    Base case: 2
    ---- staircase(2) ---- END
    output: 13
    ---- staircase(5) ---- END
    ---- staircase(4) ---- START
    ---- staircase(3) ---- START
    Base case: 4
    ---- staircase(3) ---- END
    ---- staircase(2) ---- START
    Base case: 2
    ---- staircase(2) ---- END
    ---- staircase(1) ---- START
    Base case: 1
    ---- staircase(1) ---- END
    output: 7
    ---- staircase(4) ---- END
    output: 44
    ---- staircase(7) ---- END
    Pass



```python

```
