
In Python, the map concept appears as a built-in data type called a dictionary. A dictionary contains key-value pairs. Dictionaries might soon become your favorite data structure in Python—they're extremely easy to use and useful. Here's a sample of setting up a dictionary.


```python
udacity = {}
udacity['u'] = 1
udacity['d'] = 2
udacity['a'] = 3
udacity['c'] = 4
udacity['i'] = 5
udacity['t'] = 6
udacity['y'] = 7

print (udacity)
# {'u': 1, 'd': 2, 'a': 3, 'c': 4, 'i': 5, 't': 6, 'y': 7}
```

    {'u': 1, 'd': 2, 'a': 3, 'c': 4, 'i': 5, 't': 6, 'y': 7}


In this case, the letters in "udacity" were each keys in our dictionary, and the position of that letter in the string was the value. Thus, I can do the following:


```python
print (udacity['t'])
# 6
```

    6


This statement is saying "go to the key labeled 't' and find it's value, 6".

Dictionaries are wonderfully flexible—you can store a wide variety of structures as values. You store another dictionary or a list:


```python
dictionary = {}
dictionary['d'] = [1]
dictionary['i'] = [2]
dictionary['c'] = [3]
dictionary['t'] = [4]
dictionary['i'].append(5)
dictionary['o'] = [6]
dictionary['n'] = [7]
dictionary['a'] = [8]
dictionary['r'] = [9]
dictionary['y'] = [10]
print (dictionary)
# {'d': [1], 'i': [2, 5], 'c': [3], 't': [4], 'o': [6], 'n': [7], 'a': [8], 'r': [9], 'y':[10]}
```

    {'d': [1], 'i': [2, 5], 'c': [3], 't': [4], 'o': [6], 'n': [7], 'a': [8], 'r': [9], 'y': [10]}


Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)

locations = {'North America': {'USA': ['Mountain View']}}

Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:

```
1
American City
American City
2
Asian City - Country
Asian City - Country
```


```python
# Code

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore'], 'China': ['Shanghai']}
locations['Africa'] = {'Egypt': ['Cairo']}

print(locations['North America'])

# TODO: Print a list of all cities in the USA in alphabetic order.
usa_loc = locations['North America']['USA']
usa_loc.sort()
print (1)
for city in usa_loc:
    print (city)


# TODO: Print all cities in Asia, in alphabetic order, next to the name of the country
asia_loc = locations['Asia']
asia_loc_list = [element + '-' + str(*asia_loc['India']) for element in asia_loc]
asia_loc_list.sort()
print (2)
for country_city in asia_loc_list:
    print (country_city)

```

    {'USA': ['Mountain View', 'Atlanta']}
    1
    Atlanta
    Mountain View
    2
    China-Bangalore
    India-Bangalore


<span class="graffiti-highlight graffiti-id_4ar8d9w-id_ft4syq0"><i></i><button>Hide Solution</button></span>


```python
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

usa_sorted = sorted(locations['North America']['USA'])
print (1)
for city in usa_sorted:
    print (city)

asia_cities = []
print (2)
for countries, cities in locations['Asia'].items():
    city_country = cities[0] + " - " + countries 
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print (city)

```

    1
    Atlanta
    Mountain View
    2
    Bangalore - India
    Shanghai - China



```python

```
