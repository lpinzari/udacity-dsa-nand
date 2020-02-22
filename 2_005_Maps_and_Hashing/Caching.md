
Caching can be defined as the process of storing data into a temporary data storage to avoid recomputation or to avoid reading the data from a relatively slower part of memory again and again. Thus cachig serves as a fast "look-up" storage allowing programs to execute faster.  

Let's use caching to chalk out an efficient solution for a problem.

### Problem Statement

A child is running up a staircase with and can hop either 1 step, 2 steps or 3 steps at a time. 
If the staircase has `n` steps, write a function to count the number of possible ways in which child can run up the stairs. 

For e.g. 

* `n == 1` then `answer = 1`

* `n == 3` then `answer = 4`
 
* `n == 5` then `answer = 13`


```python
def staircase(n):
    # Base Case - minimum steps possible and number of ways the child can climb them

    # Inductive Hypothesis - ways to climb rest of the steps
    
    # Inductive Step - use Inductive Hypothesis to formulate a solution
    print('staircase({})'.format(n))
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
```


```python
def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")
            
```


```python
test_case = [4, 7]
test_function(test_case)
```

    staircase(4)
    staircase(3)
    staircase(2)
    staircase(1)
    Pass



```python
test_case = [5, 13]
test_function(test_case)
```

    staircase(5)
    staircase(4)
    staircase(3)
    staircase(2)
    staircase(1)
    staircase(3)
    staircase(2)
    Pass



```python
test_case = [3, 4]
test_function(test_case)
```

    staircase(3)
    Pass



```python
test_case = [20, 121415]
test_function(test_case)
```

    Pass


<span class="graffiti-highlight graffiti-id_r189hz6-id_vtju73f"><i></i><button>Hide Solution</button></span>


```python
def staircase(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

```

### Problem Statement

While using recursion for the above problem, you might have noticed a small problem with efficiency.

Let's take a look at an example.

* Say the total number of steps are `5`. This means that we will have to call at `(n=4), (n=3), and (n=2)`

* To calculate the answer for `n=4`, we would have to call `(n=3), (n=2) and (n=1)`

You can notice that even for a small number of staircases (here 5), we are calling `n=3` and `n=2` multiple times. Each time we call a method, additional time is required to calculate the solution. In contrast, instead of calling on a particular value of `n` again and again, we can calculate it once and store the result to speed up our program.

Your job is to use any data-structure that you have used until now to write a faster implementation of the function you wrote earlier while using recursion. 



```python
def staircase(n):
    num_dict = dict({})
    return staircase_faster(n, num_dict)

def staircase_faster(n, num_dict):
    print('staircase({})'.format(n))
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        else:
            first_output =  staircase_faster(n - 1, num_dict)
        
        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)
            
        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)
        
        output = first_output + second_output + third_output
    
    num_dict[n] = output;
    return output
```


```python
test_case = [4, 7]
test_function(test_case)
```

    staircase(4)
    staircase(3)
    staircase(2)
    staircase(1)
    Pass



```python
test_case = [5, 13]
test_function(test_case)
```

    staircase(5)
    staircase(4)
    staircase(3)
    staircase(2)
    staircase(1)
    Pass



```python
test_case = [3, 4]
test_function(test_case)
```

    staircase(3)
    Pass



```python
test_case = [20, 121415]
test_function(test_case)
```

    staircase(20)
    staircase(19)
    staircase(18)
    staircase(17)
    staircase(16)
    staircase(15)
    staircase(14)
    staircase(13)
    staircase(12)
    staircase(11)
    staircase(10)
    staircase(9)
    staircase(8)
    staircase(7)
    staircase(6)
    staircase(5)
    staircase(4)
    staircase(3)
    staircase(2)
    staircase(1)
    Pass


<span class="graffiti-highlight graffiti-id_0n79ls8-id_6t02ke7"><i></i><button>Hide Solution</button></span>


```python
def staircase(n):
    num_dict = dict({})
    return staircase_faster(n, num_dict)

def staircase_faster(n, num_dict):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        else:
            first_output =  staircase_faster(n - 1, num_dict)
        
        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)
            
        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)
        
        output = first_output + second_output + third_output
    
    num_dict[n] = output;
    return output


```
