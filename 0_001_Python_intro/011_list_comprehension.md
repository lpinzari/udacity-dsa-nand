# List Comprehensions
In Python, you can create lists really quickly and concisely with list comprehensions.

```python
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
```
can be reduced to:

```python
capitalized_cities = [city.title() for city in cities]
```

List comprehensions allow us to **create a list using a `for` loop in one step**.

You create a list comprehension with brackets `[]`, including an *expression* to evaluate for each element in an iterable. This list comprehension above calls `city.title()` for each element city in cities, to create each element in the new list,`capitalized_cities`.

**Conditionals in List Comprehensions**
You can also add conditionals to list comprehensions (listcomps). After the iterable, you can use the `if` keyword to check a condition in each iteration.

```python
squares = [x**2 for x in range(9) if x % 2 == 0]
```

The code above sets squares equal to the list `[0, 4, 16, 36, 64]`, as x to the power of 2 is only evaluated if x is even. If you want to add an `else`, you will get a syntax error doing this.

```python
squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]
```

If you would like to add `else`, you have to move the conditionals to the beginning of the listcomp, right after the expression, like this.

```python
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
```

List comprehensions are not found in other languages, but are very common in Python.

## Quiz: Extract First Names
Use a list comprehension to create a new list `first_names` containing just the first names in `names` in lowercase.

```python
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)
```

Output:

```python
['rick', 'morty', 'summer', 'jerry', 'beth']
```

## Quiz: Multiples of Three
Use a list comprehension to create a list `multiples_3` containing the first 20 multiples of 3.

```python
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)
```

Output:

```python
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
```

## Quiz: Filter Names by Scores
Use a list comprehension to create a list of names `passed` that only include those that scored at least 65.

```python
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
```

Output:
The order of elements in this output may vary since dictionaries are unordered.

```python
['Beth Smith', 'Summer Smith', 'Rick Sanchez']
```

## QUESTIONS
The following questions are based on data on Oscar Award Nominations for Best Director between the years 1931 to 2010. To start you off, we've provided a dictionary called "nominated" with the year (as key) and list of directors who were nominated in that year (as value). We've provided you with a different dictionary called "winners" with the year (as key) and list of directors who won the award in that year (as value).

Question 1.
A. Create a dictionary that includes the count of Oscar nominations for each director in the nominations list.

B. Provide a dictionary with the count of Oscar wins for each director in the winners list.

```python
nominated = {1931: ['Norman Taurog', 'Wesley Ruggles', 'Clarence Brown', 'Lewis Milestone', 'Josef Von Sternberg'],
             1932: ['Frank Borzage', 'King Vidor', 'Josef Von Sternberg'],
             1933: ['Frank Lloyd', 'Frank Capra', 'George Cukor'],
             1934: ['Frank Capra', 'Victor Schertzinger', 'W. S. Van Dyke'],
             1935: ['John Ford', 'Michael Curtiz', 'Henry Hathaway', 'Frank Lloyd'],
             1936: ['Frank Capra', 'William Wyler', 'Robert Z. Leonard', 'Gregory La Cava', 'W. S. Van Dyke'],
             1937: ['Leo McCarey', 'Sidney Franklin', 'William Dieterle', 'Gregory La Cava', 'William Wellman'],
             1938: ['Frank Capra', 'Michael Curtiz', 'Norman Taurog', 'King Vidor', 'Michael Curtiz'],
             1939: ['Sam Wood', 'Frank Capra', 'John Ford', 'William Wyler', 'Victor Fleming'],
             1940: ['John Ford', 'Sam Wood', 'William Wyler', 'George Cukor', 'Alfred Hitchcock'],
             1941: ['John Ford', 'Orson Welles', 'Alexander Hall', 'William Wyler', 'Howard Hawks'],
             1942: ['Sam Wood', 'Mervyn LeRoy', 'John Farrow', 'Michael Curtiz', 'William Wyler'],
             1943: ['Michael Curtiz', 'Ernst Lubitsch', 'Clarence Brown', 'George Stevens', 'Henry King'],
             1944: ['Leo McCarey', 'Billy Wilder', 'Otto Preminger', 'Alfred Hitchcock', 'Henry King'],
             1945: ['Billy Wilder', 'Leo McCarey', 'Clarence Brown', 'Jean Renoir', 'Alfred Hitchcock'],
             1946: ['David Lean', 'Frank Capra', 'Robert Siodmak', 'Clarence Brown', 'William Wyler']}
winners = {1931: ['Norman Taurog'],
          1932: ['Frank Borzage'],
          1933: ['Frank Lloyd'],
          1934: ['Frank Capra'],
          1935: ['John Ford'],
          1936: ['Frank Capra'],
          1937: ['Leo McCarey'],
          1938: ['Frank Capra'],
          1939: ['Victor Fleming'],
          1940: ['John Ford'],
          1941: ['John Ford'],
          1942: ['William Wyler'],
          1943: ['Michael Curtiz'],
          1944: ['Leo McCarey'],
          1945: ['Billy Wilder'],
          1946: ['William Wyler']}

```

Question 1A:

```python
### 1A: Create dictionary with the count of Oscar nominations for each director
nom_count_dict = {}
# Add your code here

for year, directors in nominated.items():
    for director in directors:
        if director not in nom_count_dict:
            nom_count_dict[director] = 1
        else:
            nom_count_dict[director] += 1

print("nom_count_dict = {}\n".format(nom_count_dict))
```

Here's the logic for my solution:
1. To solve this question, I use the `.items` method for dictionaries. Remember, the key in our nominated dictionary is a list of nominated directors. Think Compound Data Structures!
2. I know I need to create a dictionary where the key is a director and the value is the number of nominations.
3. But to get each director as a key, I will have to use two for loops.
First, to iterate through the nominated dictionary's value (which here is a list of nominations) .
4. But I have do to this again to iterate through each element (what I'm trying to get to - a nominated director) in the nominated list.
5. After that, if the director isn't yet in our dictionary, we give that director a count of one. If the director is in the dictionary, we increment that director's count by one.

Question 1B:
Provide a dictionary with the count of wins for each director.

Essentially, it is the same logic as above, with the other dictionary.
We could use the same approach as in question 1a and it would work fine, but I've provided a shorter alternative here. Instead of the last 4 lines as above, I've just written 1 line, by using the `.get` method. In this line, we find the director in the `win_count_dict` dictionary and return the value for that director (the number of times they've won). If they aren't in the dictionary, get returns 0 for that director. Then we increment that director's count by one.

```python
win_count_dict = {}
for year, winnerlist in winners.items():
    for winner in winnerlist:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1
```

Question 2:
Provide a list with the name(s) of the director(s) with the most Oscar wins. We are asking for a list because there could be more than 1 director tied for the most Oscar wins.

Here's the logic for my solution:
1. To address this question, I will need to first create a dictionary with the number of wins by each winning director. For that I can use the code we wrote for Question 1b above.

```python
#FIRST PART OF SOLUTION
win_count_dict = {}
for year, winnerlist in winners.items():
    for winner in winnerlist:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1
```

2. This `win_count_dict` dictionary provides a dictionary with the win count for the directors. We will need this to then identify which key (here, director name) has the highest value (here, win count).
3. To perform this task, we use a variable `highest_count` to keep track of the highest count of wins.
4. We iterate through the dictionary to see if the value for a key (i.e., wins for a director) is more than the highest count.
5. If it is, we replace that value as the highest_count.
6. Plus we add that key (here, director name) to our list tracking the most_win_director.
7. Every time we come upon a value higher than the current highest_count, we replace highest_count with the new higher value, empty the most_win_director and replace it with the new key (i.e., director's name).

```python
#SECOND PART OF SOLUTION
highest_count = 0
most_win_director = []

for key, value in win_count_dict.items():
    if value > highest_count:
        highest_count = value
        most_win_director.clear()
        most_win_director.append(key)
    elif value == highest_count:
        most_win_director.append(key)
    else:
        continue
```

**Here is an alternative compact solution** to replace the 12 lines above for the second part of the solution, using the built-in function `max()`, and a list comprehension with a condition:

```python
#ALTERNATIVE SECOND PART OF SOLUTION
highest_count = max(win_count_dict.values())

most_win_director = [key for key, value in win_count_dict.items() if value == highest_count]
```
