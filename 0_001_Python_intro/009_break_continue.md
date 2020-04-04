# Break, Continue
Sometimes we need more control over when a loop should end, or skip an iteration. In these cases, we use the `break` and `continue` **keywords**, which can be used in both for and while loops.

- **break** terminates a loop
- **continue** skips one iteration of a loop


## Quiz: Break the String
Write a `loop` with a `break` statement to create a string, `news_ticker`, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that `news_ticker` is exactly 140 characters long.

Remember that break works in both for and while loops. Use whichever loop seems most appropriate.
```python
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)
```

## Coding Quiz: Check for Prime Numbers
Question: Write code to check if the numbers provided in the list `check_prime` are prime numbers. For each number, if the number is prime, the code should print that the number is a prime number. If the number is NOT a prime number, it should print that the number is not a prime number, and also print a factor of that number besides 1 and the number itself.

**Logic for our solution**:

- We loop through each number in the `check_prime list`.
- Create a "search-for-factors" loop beginning at 2, and continuing up to the (number-1)
- Use a conditional statement with the modulo operator to check if our number when divided by the possible factor yields any remainder besides 0.
- If we ever find one factor, we can declare that the number is not prime, and state the factor we found. Then we can break out of the loop for that number.
- If we get up to the (number - 1) and haven't broken out of the loop, then we can declare that the number is prime.

```python
check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break

# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:    
            print("{} IS a prime number".format(num))
```
