# Binary search
Binary search is probably one of the most common algorithms that we all use without even realizing we are using it.

To help build a little intuition for how it works, let's first look at a classic game where the most efficient way to win is to use binary search.

# Guess the number

This notebook simulates a classic game where you have to guess a random number from within a certain range. Typically, you might have to guess a number from 1 to 10, and have three guesses to get the right answer.

In this case, you'll need to guess a random number between 1 and 100, and you will have 7 tries.

Try running it and playing a round or two. Notice that the game always tells you whether your guess was too high or too low. This information allows you to rule out some of the numbers (so that you don't waste time guessing those numbers).

With this fact in mind, try to make your guesses in the most efficient way you can. Specifically, try to make guesses that rule out the largest number of possibilities each time.


```python
import random

def guess_the_number(total_tries, start_range, end_range):
    if start_range > end_range:
        start_range, end_range = end_range, start_range

    random_number = random.randint(start_range, end_range)
    try_count = 0
    success_message = "Awesome! You guessed correctly"
    failure_message = "Sorry! No more retries left"
    miss_message = "Oops! That's incorrect"

    num_tries = 0
    while num_tries < total_tries:
        attempt = int(input("Guess the number: "))

        if attempt == random_number:
            print(success_message)
            return
        print(miss_message)
        if attempt < random_number:
            print("Go higher!")
        else:
            print("Go lower!")
        num_tries += 1
    print(failure_message)

total_tries = 7
start_range = 1
end_range = 100
guess_the_number(total_tries, start_range, end_range)
```

    Guess the number: 50
    Oops! That's incorrect
    Go higher!
    Guess the number: 75
    Oops! That's incorrect
    Go higher!
    Guess the number: 87
    Oops! That's incorrect
    Go higher!
    Guess the number: 93
    Oops! That's incorrect
    Go lower!
    Guess the number: 90
    Oops! That's incorrect
    Go higher!
    Guess the number: 92
    Oops! That's incorrect
    Go lower!
    Guess the number: 91
    Awesome! You guessed correctly

Obviously, there is some randomness involved in this game, so in some cases you may run out of tries before guessing correctly. However, if you use a binary search strategy, you'll find the number efficiently and win most of the time.

But before we look further into binary search, let's first look at an alternative: *Linear search*.

# Linear search
Suppose that you have a dictionary of words and that you need to look up a particular word in this dictionary. However, this dictionary is a pretty terrible dictionary, because the words are all in a scrambled order (and not alphabetical as they usually are). What search strategy would you use to find the definition you're looking for?

Because the words are in a random order, the best we can do is simply to go one by one, from the first page to the last page, in a sequential manner. Sounds tedious, right? This is called **linear search**. We have no idea about the order of the words, so we simply have to flip through the pages, one by one, until we find the word we are looking for.

With the example of the guessing game, you could use linear search there as well—by simply starting with 1 and guessing every number until you get to 100 (or rather, until you run out of tries and lose the game!).

Question 1:

- What would the time complexity be for linear search?

(Think about the worst case scenario, where the word you're looking for is on the last page of the dictionary.) Solution: **O(n)**

# Back to binary search
Now let's consider a different scenario: Similar to the above, we have a dictionary and a word that we want to find in that dictionary. But this time, the dictionary is sorted in alphabetical order (just as you would expect from any decent dictionary). We still don't know what page our word is on, so we'll need to search for it—but the fact that the dictionary is sorted changes the strategy we should use.

Question 2:

You're going to make your first guess about which page the word might be on. Then you'll open the dictionary and take a look to see if you're right.

- Which page should you look at first? (Assuming you want to find the word as quickly as possible.) Solution: **The middle page (half through the dictionary)**

*Note*: With a real dictionary, we might have some idea about the approximate location of a word. For example, if the word is "aardvark", we know it is going to be close to the beginning of the dictionary, while if it is "zebra", we know it will be close to the end. For the purposes of this example, we're going to ignore this kind of information.

Of the above options, the best strategy we can take is to open the dictionary in the middle.

Then, we do the following:

- Compare the target word with the words on this page.
- If the target word comes earlier (in terms of alphabetical order), then we discard the right half of the book. From now on, we will only search in the left half.
- Similarly, if the word comes later than the words on this page, then we discard the left half of the book. From now on, we will only search in the right half.

Whatever happens, we are guaranteed to be able to discard half of the search space in this first step alone.

Next, we repeat this process. We take the remaining half of the dictionary and we open it to the middle page. We then discard the left or right half, and repeat again. We continue this process, eliminating half of the search space at each step, until we find the target word. This is **binary search**.

Note that the word binary means "having two parts". Binary search means we are doing a search where, at each step, we divide the input into two parts. Also note that the data we are searching through has to be sorted.

Let's see what this would look like on a real data structure, such as an array:

*video_1*

In summary:

- Binary search is a search algorithm where we find the position of a target value by comparing the middle value with this target value.
- If the middle value is equal to the target value, then we have our solution (we have found the position of our target value).
- If the target value comes before the middle value, we look for the target value in the left half.
- Otherwise, we look for the target value in the right half.
- We repeat this process as many times as needed, until we find the target value.
