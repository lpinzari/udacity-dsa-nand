# Practice Debugging
In the example at the bottom of the page, there is a piece of code in the `user_input_numlist.py` Python file. The code prompts the user to enter 10 two-digit numbers. It should then find and print the sum of all of the even numbers among those that were entered.

But there is a bug in the code! When I input a number, I get the following **TypeError**.

```console
Enter any 2 digit number: 23
Traceback (most recent call last):
  File "...", line 8, in <module>
    if number % 2 == 0:
TypeError: not all arguments converted during string formatting
```

Sample Output: This is what the output should look like.

```console
>>> user_list: [23, 24, 25, 26, 27, 28, 29, 30, 31, 22]
>>> The sum of the even numbers in user_list is: 130.
```


**user_input_numlist.py**

```python
# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers
for i in range(10):
    userInput = (int)(input("Enter any 2-digit number: "))

# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    try:
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))
```
