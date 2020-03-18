
# Coin Change

You are given coins of different denominations and a total amount of money. Write a function to compute the fewest coins needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

As an example:
* Input: `coins = [1, 2, 3]`, `amount = 6`
* Output: `2`
* Explanation: The output is `2` because we can use `2` coins with value `3`. That is, `6 = 3 + 3`. We could also use `3` coins with value `2` (that is, `6 = 2 + 2 + 2`), but this would use more coins—and the problem specifies we should use the smallest number of coins possible.

There's test code below that you can use to check your solution. And at the bottom of the notebook, you'll find two different possible solutions.


```python
import sys

def coin_change(coins, amount):

    # TODO: Complete the coin_change function
    # This should return one value: the fewest coins needed to make up the given amount
    # Create a memo that will storing the fewest coins with given amount
    # that we have already calculated so that we do not have to do the
    # calculation again.
    
    m = len(coins)
    memo = {}
    
    def minCoins(coins, m, amount):
        
        print ('START: minCoins(coins, m, {})'.format(amount))
        # Base case:
        if amount == 0:
            print ('       minCoins(coins, m, {}): 0 COINS'.format(amount))
            return 0
        
        # Initialize result
        res = float('inf')
        
        # Check if we have already calculated
        if amount not in memo:
            # Try every coin that has smaller value than amount
            for i in range(0,m):
                print ('       minCoins(coins, m, {}): -- i: {} coin {}'.format(amount,i,coins[i]), end=" ")
                if (coins[i] <= amount):
                    print('({} <= {})'.format(coins[i],amount))
                    sub_res = minCoins(coins, m, amount - coins[i])
                
                    # Check for INT_MAX to avoid overflow and see if result can be minimized
                    if (sub_res != float('inf') and sub_res + 1 < res):
                        res = sub_res + 1
                else:
                    print('({} > {})'.format(coins[i],amount))
                print ('       minCoins(coins, m, {}): -- i: {} coin {} res {}'.format(amount,i,coins[i],res))
            memo[amount] = res
            print ('       minCoins(coins, m, {}): {} COINS'.format(amount,res))
            return res
        
        print ('       minCoins(coins, m, {}): {} COINS \t ALREADY COMPUTED'.format(amount,memo[amount]))
        return memo[amount]
    
    res = minCoins(coins, m, amount)
    # return -1 when no change found
    return -1 if res == float('inf') else res

```


```python
def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
```


```python
arr = [1,2,3]
amount = 6
solution = 2

# arr = [1,2,5]
# amount = 11
# solution = 3
test_case = [arr, amount, solution]
test_function(test_case)
```

    START: minCoins(coins, m, 6)
           minCoins(coins, m, 6): -- i: 0 coin 1 (1 <= 6)
    START: minCoins(coins, m, 5)
           minCoins(coins, m, 5): -- i: 0 coin 1 (1 <= 5)
    START: minCoins(coins, m, 4)
           minCoins(coins, m, 4): -- i: 0 coin 1 (1 <= 4)
    START: minCoins(coins, m, 3)
           minCoins(coins, m, 3): -- i: 0 coin 1 (1 <= 3)
    START: minCoins(coins, m, 2)
           minCoins(coins, m, 2): -- i: 0 coin 1 (1 <= 2)
    START: minCoins(coins, m, 1)
           minCoins(coins, m, 1): -- i: 0 coin 1 (1 <= 1)
    START: minCoins(coins, m, 0)
           minCoins(coins, m, 0): 0 COINS
           minCoins(coins, m, 1): -- i: 0 coin 1 res 1
           minCoins(coins, m, 1): -- i: 1 coin 2 (2 > 1)
           minCoins(coins, m, 1): -- i: 1 coin 2 res 1
           minCoins(coins, m, 1): -- i: 2 coin 3 (3 > 1)
           minCoins(coins, m, 1): -- i: 2 coin 3 res 1
           minCoins(coins, m, 1): 1 COINS
           minCoins(coins, m, 2): -- i: 0 coin 1 res 2
           minCoins(coins, m, 2): -- i: 1 coin 2 (2 <= 2)
    START: minCoins(coins, m, 0)
           minCoins(coins, m, 0): 0 COINS
           minCoins(coins, m, 2): -- i: 1 coin 2 res 1
           minCoins(coins, m, 2): -- i: 2 coin 3 (3 > 2)
           minCoins(coins, m, 2): -- i: 2 coin 3 res 1
           minCoins(coins, m, 2): 1 COINS
           minCoins(coins, m, 3): -- i: 0 coin 1 res 2
           minCoins(coins, m, 3): -- i: 1 coin 2 (2 <= 3)
    START: minCoins(coins, m, 1)
           minCoins(coins, m, 1): 1 COINS 	 ALREADY COMPUTED
           minCoins(coins, m, 3): -- i: 1 coin 2 res 2
           minCoins(coins, m, 3): -- i: 2 coin 3 (3 <= 3)
    START: minCoins(coins, m, 0)
           minCoins(coins, m, 0): 0 COINS
           minCoins(coins, m, 3): -- i: 2 coin 3 res 1
           minCoins(coins, m, 3): 1 COINS
           minCoins(coins, m, 4): -- i: 0 coin 1 res 2
           minCoins(coins, m, 4): -- i: 1 coin 2 (2 <= 4)
    START: minCoins(coins, m, 2)
           minCoins(coins, m, 2): 1 COINS 	 ALREADY COMPUTED
           minCoins(coins, m, 4): -- i: 1 coin 2 res 2
           minCoins(coins, m, 4): -- i: 2 coin 3 (3 <= 4)
    START: minCoins(coins, m, 1)
           minCoins(coins, m, 1): 1 COINS 	 ALREADY COMPUTED
           minCoins(coins, m, 4): -- i: 2 coin 3 res 2
           minCoins(coins, m, 4): 2 COINS
           minCoins(coins, m, 5): -- i: 0 coin 1 res 3
           minCoins(coins, m, 5): -- i: 1 coin 2 (2 <= 5)
    START: minCoins(coins, m, 3)
           minCoins(coins, m, 3): 1 COINS 	 ALREADY COMPUTED
           minCoins(coins, m, 5): -- i: 1 coin 2 res 2
           minCoins(coins, m, 5): -- i: 2 coin 3 (3 <= 5)
    START: minCoins(coins, m, 2)
           minCoins(coins, m, 2): 1 COINS 	 ALREADY COMPUTED
           minCoins(coins, m, 5): -- i: 2 coin 3 res 2
           minCoins(coins, m, 5): 2 COINS
           minCoins(coins, m, 6): -- i: 0 coin 1 res 3
           minCoins(coins, m, 6): -- i: 1 coin 2 (2 <= 6)
    START: minCoins(coins, m, 4)
           minCoins(coins, m, 4): 2 COINS 	 ALREADY COMPUTED
           minCoins(coins, m, 6): -- i: 1 coin 2 res 3
           minCoins(coins, m, 6): -- i: 2 coin 3 (3 <= 6)
    START: minCoins(coins, m, 3)
           minCoins(coins, m, 3): 1 COINS 	 ALREADY COMPUTED
           minCoins(coins, m, 6): -- i: 2 coin 3 res 2
           minCoins(coins, m, 6): 2 COINS
    Pass



```python

# arr = [1,4,5,6]
# amount = 23
# solution = 4
# test_case = [arr, amount, solution]
# test_function(test_case)
```

    4



```python
arr = [5,7,8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)
```

    minCoins(coins, m, 2)
    Pass


## Solutions

Let's look at two different solutions. Here's one way to do it...

<span class="graffiti-highlight graffiti-id_jjdrdzm-id_fpk926y"><i></i><button>Hide Solution One</button></span>


```python
# Solution One

# Let's assume F(Amount) is the minimum number of coins needed to make a change from coins [C0, C1, C2...Cn-1]
# Then, we know that F(Amount) = min(F(Amount-C0), F(Amount-C1), F(Amount-C2)...F(Amount-Cn-1)) + 1

# Base Cases: 
    # when Amount == 0: F(Amount) = 0
    # when Amount < 0: F(Amount) =  float('inf')

def coin_change(coins, amount):
    # Create a memo that will storing the fewest coins with given amount
    # that we have already calculated so that we do not have to do the
    # calculation again.
    memo = {}
    
    def return_change(remaining):
        # Base cases
        if remaining < 0:  return float('inf')
        if remaining == 0: return 0 
        
        # Check if we have already calculated
        if remaining not in memo:
            # If not previously calculated, calculate it by calling return_change with the remaining amount
            memo[remaining] = min(return_change(remaining - c) + 1 for c in coins)
        return memo[remaining]
    
    res = return_change(amount)
    
    # return -1 when no change found
    return -1 if res == float('inf') else res

```

And here's another possibility:

<span class="graffiti-highlight graffiti-id_bmrwntc-id_9z3z0e0"><i></i><button>Hide Solution Two</button></span>


```python
# Solution Two

# We initiate F[Amount] to be float('inf') and F[0] = 0
# Let F[Amount] to be the minimum number of coins needed to get change for the Amount.
# F[Amount + coin] = min(F(Amount + coin), F(Amount) + 1) if F[Amount] is reachable.
# F[Amount + coin] = F(Amount + coin) if F[Amount] is not reachable.

def coin_change2(coins, amount):
    # initiate the list with length amount + 1 and prefill with float('inf')
    res = [float('inf')]*(amount + 1)
    
    print('res: {}'.format(res))
    # when amount = 0, 0 number of coins will be needed for the change
    res[0] = 0
    print('res: {}'.format(res))
    
    i = 0
    while (i < amount):
        print ('\n i: {} (amount)'.format(i))
        if res[i] != float('inf'):
            for coin in coins:
                print ('\t coin: {}'.format(coin), end = " ")
                if i <= amount - coin:
                    print ('   {} <= {} - {}'.format(i, amount, coin), end = "  ")
                    print ('res[{}+{}] = min(res[{}] + 1, res[{}+{}])'.format(i,coin,i,i,coin), end = "  ")
                    res[i+coin] = min(res[i] + 1, res[i+coin])
                    print (res)
        i += 1

    if res[amount] == float('inf'):
        return -1
    return res[amount]
        
arr = [1,2,3]
amount = 6
solution = 2
output = coin_change2(arr, amount)
print(output)
```

    res: [inf, inf, inf, inf, inf, inf, inf]
    res: [0, inf, inf, inf, inf, inf, inf]
    
     i: 0 (amount)
    	 coin: 1    0 <= 6 - 1  res[0+1] = min(res[0] + 1, res[0+1])  [0, 1, inf, inf, inf, inf, inf]
    	 coin: 2    0 <= 6 - 2  res[0+2] = min(res[0] + 1, res[0+2])  [0, 1, 1, inf, inf, inf, inf]
    	 coin: 3    0 <= 6 - 3  res[0+3] = min(res[0] + 1, res[0+3])  [0, 1, 1, 1, inf, inf, inf]
    
     i: 1 (amount)
    	 coin: 1    1 <= 6 - 1  res[1+1] = min(res[1] + 1, res[1+1])  [0, 1, 1, 1, inf, inf, inf]
    	 coin: 2    1 <= 6 - 2  res[1+2] = min(res[1] + 1, res[1+2])  [0, 1, 1, 1, inf, inf, inf]
    	 coin: 3    1 <= 6 - 3  res[1+3] = min(res[1] + 1, res[1+3])  [0, 1, 1, 1, 2, inf, inf]
    
     i: 2 (amount)
    	 coin: 1    2 <= 6 - 1  res[2+1] = min(res[2] + 1, res[2+1])  [0, 1, 1, 1, 2, inf, inf]
    	 coin: 2    2 <= 6 - 2  res[2+2] = min(res[2] + 1, res[2+2])  [0, 1, 1, 1, 2, inf, inf]
    	 coin: 3    2 <= 6 - 3  res[2+3] = min(res[2] + 1, res[2+3])  [0, 1, 1, 1, 2, 2, inf]
    
     i: 3 (amount)
    	 coin: 1    3 <= 6 - 1  res[3+1] = min(res[3] + 1, res[3+1])  [0, 1, 1, 1, 2, 2, inf]
    	 coin: 2    3 <= 6 - 2  res[3+2] = min(res[3] + 1, res[3+2])  [0, 1, 1, 1, 2, 2, inf]
    	 coin: 3    3 <= 6 - 3  res[3+3] = min(res[3] + 1, res[3+3])  [0, 1, 1, 1, 2, 2, 2]
    
     i: 4 (amount)
    	 coin: 1    4 <= 6 - 1  res[4+1] = min(res[4] + 1, res[4+1])  [0, 1, 1, 1, 2, 2, 2]
    	 coin: 2    4 <= 6 - 2  res[4+2] = min(res[4] + 1, res[4+2])  [0, 1, 1, 1, 2, 2, 2]
    	 coin: 3 
     i: 5 (amount)
    	 coin: 1    5 <= 6 - 1  res[5+1] = min(res[5] + 1, res[5+1])  [0, 1, 1, 1, 2, 2, 2]
    	 coin: 2 	 coin: 3 2



```python

```
