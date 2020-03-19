
# Stock Prices

You are given access to yesterday's stock prices for a single stock. The data is in the form of an array with the stock price in 30 minute intervals from 9:30 a.m EST opening to 4:00 p.m EST closing time. With this data, write a function that returns the maximum profit obtainable. You will need to buy before you can sell.

For example, suppose you have the following prices:

`prices = [3, 4, 7, 8, 6]`

>Note: This is a shortened array, just for the sake of example—a full set of prices for the day would have 13 elements (one price for each 30 minute interval betwen 9:30 and 4:00), as seen in the test cases further down in this notebook.

In order to get the maximum profit in this example, you would want to buy at a price of 3 and sell at a price of 8 to yield a maximum profit of 5. In other words, you are looking for the greatest possible difference between two numbers in the array.

Fill out the function below and run it against the test cases. Take into consideration the time complexity of your solution. 


```python
def max_returns(prices):
    """
    Calculate maxiumum possible return
    
    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """
    
    return prices
```

<span class="graffiti-highlight graffiti-id_uc722im-id_o4cterg"><i></i><button>Hide Solution</button></span>


```python
# Solution

def max_returns(arr):
    """
    The idea is to pick two dates:
        1. buy date
        2. sell date
    We will keep track of our max profit while iterating over the list
    At each step we will make the greedy choice by choosing prices such that our profit is maximum 
    """
    # initialize the pointers to the first two elements in the array
    min_price_index = 0 # first element in the array
    max_price_index = 1 # second element in the array
    current_min_price_index = 0 # the first element
    
    print (arr)
    print ('min_idx: {} \t max_idx: {} \t current_min_idx: {}'.format(min_price_index,max_price_index,current_min_price_index))
    
    if len(arr) < 2:
        return None
    
    for index in range(1, len(arr)):
        
        print ('i: {} value: {}'.format(index,arr[index]))
        # current minimum price
        if arr[index] < arr[current_min_price_index]:
            current_min_price_index = index
            
        # current max profit: compare the old maximum profit with the current profit
        if arr[max_price_index] - arr[min_price_index] < arr[index] - arr[current_min_price_index]:
            max_price_index = index
            min_price_index = current_min_price_index
            
        print ('min_idx: {} \t max_idx: {} \t current_min_idx: {}'.format(min_price_index,max_price_index,current_min_price_index), end =" ")
        print ('profit: {} - {} = {}'.format(arr[max_price_index],arr[min_price_index],arr[max_price_index] - arr[min_price_index]))
    max_profit = arr[max_price_index] - arr[min_price_index]
    return max_profit
```


```python
# Test Cases
def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
```


```python
prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
test_function(test_case)
```

    [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
    min_idx: 0 	 max_idx: 1 	 current_min_idx: 0
    i: 1 value: 2
    min_idx: 0 	 max_idx: 1 	 current_min_idx: 0 profit: 2 - 2 = 0
    i: 2 value: 7
    min_idx: 0 	 max_idx: 2 	 current_min_idx: 0 profit: 7 - 2 = 5
    i: 3 value: 9
    min_idx: 0 	 max_idx: 3 	 current_min_idx: 0 profit: 9 - 2 = 7
    i: 4 value: 9
    min_idx: 0 	 max_idx: 3 	 current_min_idx: 0 profit: 9 - 2 = 7
    i: 5 value: 12
    min_idx: 0 	 max_idx: 5 	 current_min_idx: 0 profit: 12 - 2 = 10
    i: 6 value: 18
    min_idx: 0 	 max_idx: 6 	 current_min_idx: 0 profit: 18 - 2 = 16
    i: 7 value: 23
    min_idx: 0 	 max_idx: 7 	 current_min_idx: 0 profit: 23 - 2 = 21
    i: 8 value: 34
    min_idx: 0 	 max_idx: 8 	 current_min_idx: 0 profit: 34 - 2 = 32
    i: 9 value: 37
    min_idx: 0 	 max_idx: 9 	 current_min_idx: 0 profit: 37 - 2 = 35
    i: 10 value: 45
    min_idx: 0 	 max_idx: 10 	 current_min_idx: 0 profit: 45 - 2 = 43
    i: 11 value: 54
    min_idx: 0 	 max_idx: 11 	 current_min_idx: 0 profit: 54 - 2 = 52
    i: 12 value: 78
    min_idx: 0 	 max_idx: 12 	 current_min_idx: 0 profit: 78 - 2 = 76
    Pass



```python
prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
test_case = [prices, solution]
test_function(test_case)
```

    [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
    min_idx: 0 	 max_idx: 1 	 current_min_idx: 0
    i: 1 value: 18
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 1 profit: 18 - 18 = 0
    i: 2 value: 37
    min_idx: 1 	 max_idx: 2 	 current_min_idx: 1 profit: 37 - 18 = 19
    i: 3 value: 9
    min_idx: 1 	 max_idx: 2 	 current_min_idx: 3 profit: 37 - 18 = 19
    i: 4 value: 11
    min_idx: 1 	 max_idx: 2 	 current_min_idx: 3 profit: 37 - 18 = 19
    i: 5 value: 48
    min_idx: 3 	 max_idx: 5 	 current_min_idx: 3 profit: 48 - 9 = 39
    i: 6 value: 23
    min_idx: 3 	 max_idx: 5 	 current_min_idx: 3 profit: 48 - 9 = 39
    i: 7 value: 1
    min_idx: 3 	 max_idx: 5 	 current_min_idx: 7 profit: 48 - 9 = 39
    i: 8 value: 7
    min_idx: 3 	 max_idx: 5 	 current_min_idx: 7 profit: 48 - 9 = 39
    i: 9 value: 34
    min_idx: 3 	 max_idx: 5 	 current_min_idx: 7 profit: 48 - 9 = 39
    i: 10 value: 2
    min_idx: 3 	 max_idx: 5 	 current_min_idx: 7 profit: 48 - 9 = 39
    i: 11 value: 45
    min_idx: 7 	 max_idx: 11 	 current_min_idx: 7 profit: 45 - 1 = 44
    i: 12 value: 67
    min_idx: 7 	 max_idx: 12 	 current_min_idx: 7 profit: 67 - 1 = 66
    Pass



```python
prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
test_case = [prices, solution]
test_function(test_case)
```

    [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
    min_idx: 0 	 max_idx: 1 	 current_min_idx: 0
    i: 1 value: 54
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 1 profit: 54 - 54 = 0
    i: 2 value: 45
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 2 profit: 54 - 54 = 0
    i: 3 value: 37
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 3 profit: 54 - 54 = 0
    i: 4 value: 34
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 4 profit: 54 - 54 = 0
    i: 5 value: 23
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 5 profit: 54 - 54 = 0
    i: 6 value: 18
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 6 profit: 54 - 54 = 0
    i: 7 value: 12
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 7 profit: 54 - 54 = 0
    i: 8 value: 9
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 8 profit: 54 - 54 = 0
    i: 9 value: 9
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 8 profit: 54 - 54 = 0
    i: 10 value: 7
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 10 profit: 54 - 54 = 0
    i: 11 value: 2
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 11 profit: 54 - 54 = 0
    i: 12 value: 2
    min_idx: 1 	 max_idx: 1 	 current_min_idx: 11 profit: 54 - 54 = 0
    Pass



```python

```
