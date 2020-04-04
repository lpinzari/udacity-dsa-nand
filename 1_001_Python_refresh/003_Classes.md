# Python Classes Review
## Python Classes Overview
A class is a structure in object-oriented programming that allows functions and related data to be grouped together.

In a Python class, an important concept is `self`, which is used to reference a class instance's own variables and functions from within the class definition. For example, if we had a class called Person and we wanted the class instances to have a variable called `age`, we could store this information by using `self.age`.

Also, if we wanted the class to have a function that would increment the age of the person, we could define a function inside this class called `def birthday(self)`. In order to be a class function, birthday needs to include the input **variable `self`**, as **this is used for proper referencing within the class**.

Another important and commonly used function definition is the class **initializer**, `def __init__(self)`. The body of the initializer is where instance variable definitions should be added, and the **initializer initializes all the variables once an instance of the class is created**. Also, any input variables that a class needs to have, such as a name for the person can be passed into initializer function.

>`self` must be used when declaring a variable in an `__init__` function so that each instance of the class has its own copy of that variable.

### Examples of Python Classes
Below is an example of a basic `Person` class. The class has two variables for name and age, along with three functions for initializing the class, incrementing the person’s age, and getting the person’s name.

```python
class Person:
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age

    def birthday(self):
        self.person_age += 1

    def getName(self):
        return self.person_name
```
Let’s look at an example for how to create an instance of the `Person` class using the class template above. We can then access that `Person’s name`:

```python
bob = Person('Bob', 32)
print(bob.getName())
# prints Bob
```

Currently, we have one function for getting the class’s variable. This is called an **Accessor**. The other function that the class has is actually modifying one of the class’ variables, and that is called a **Mutator**. We can make our Person older by calling `birthday()`.

```python
bob.birthday()
print(bob.person_age)
# prints 33
```

The birthday function call successfully increments the age of our Person. Also note that we can directly get the age of bob without using a function call. This is because the `Person` class variables are defined as *public*, so we can directly access them without a function call. If instead we wanted the `Person’s age variable` to be **private** to the class, in **Python 3** we could put **double underscores** in front of the variable: **__person_age**. Then we would **have to use a function call in order to retrieve it**.

### Python Class Practice
#### Exercise 1
Now let's assume that the current month is April, and you want to use a `Person` class to help make use of information about the friends in your contacts list. In particular, you'd like to increment the age of all of your friends with birthdays in April. You would also like to know who they are, along with their current ages, so you can send them birthday cards. Finally, you would also like to figure out which month has the most friends with birthdays, so you can budget for all of the birthday cards you will need to buy.

In the following exercise, the `Person` class will be provided for you, and you will be working with a list of instances of the class, representing friends in your contacts. This **list** is stored in the variable `people`.

To complete the exercise, you will need to do two things:

1. Complete the function `get_april_birthdays(people)`. This function should return a dictionary with each name of your friend with an April birthday as a key, and their updated age as the value.
2. Complete the function `get_most_common_month(people)`. This function should return the name of the month with the most number of birthdays among your friends.
There is some testing code provided in `test()`, and there are more specific TODO instructions in each of the two functions mentioned.

```python
class Person:
    def __init__(self, name, age, month):
        self.name = name
        self.age = age
        self.birthday_month = month

    def birthday(self):
        self.age += 1

def create_person_objects(names, ages, months):
    my_data = zip(names, ages, months)
    person_objects = []
    for item in my_data:
        print(item)
        person_objects.append(Person(*item))
    return person_objects

def get_april_birthdays(people):
    # TODO:
    # Increment "age" for all people with birthdays in April.
    # Return a dictionary "april_birthdays" with the names of
    # all people with April birthdays as keys, and their updated ages
    # as values. See the test below for an example expected output.
    april_birthdays = {}
    for person in people:
        if person.birthday_month == 'April':
            person.age += 1
            april_birthdays[person.name] = person.age

    return april_birthdays

def get_most_common_month(people):
    # TODO: Use the "months" dictionary to record counts of
    # birthday months for persons in the "people" data.
    # Return the month with the largest number of birthdays.
    months = {'January':0, 'February':0, 'March':0, 'April':0, 'May':0,
              'June':0, 'July':0, 'August':0, 'September':0, 'October':0,
              'November':0, 'December':0}

    for person in people:
        months[person.birthday_month] += 1

    max_month = None
    max_value = 0
    for key in months.keys():
        if months[key] > max_value:
            max_value = months[key]
            max_month = key

    return max_month



def test():
    # Here is the data for the test. Assume there is a single most common month.
    names = ['Howard', 'Richard', 'Jules', 'Trula', 'Michael', 'Elizabeth', 'Richard', 'Shirley', 'Mark', 'Brianna', 'Kenneth', 'Gwen', 'William', 'Rosa', 'Denver', 'Shelly', 'Sammy', 'Maryann', 'Kathleen', 'Andrew', 'Joseph', 'Kathleen', 'Lisa', 'Viola', 'George', 'Bonnie', 'Robert', 'William', 'Sabrina', 'John', 'Robert', 'Gil', 'Calvin', 'Robert', 'Dusty', 'Dario', 'Joeann', 'Terry', 'Alan', 'Rosa', 'Jeane', 'James', 'Rachel', 'Tu', 'Chelsea', 'Andrea', 'Ernest', 'Erica', 'Priscilla', 'Carol', 'Michael', 'Dale', 'Arthur', 'Helen', 'James', 'Donna', 'Patricia', 'Betty', 'Patricia', 'Mollie', 'Nicole', 'Ernest', 'Wendy', 'Graciela', 'Teresa', 'Nicole', 'Trang', 'Caleb', 'Robert', 'Paul', 'Nieves', 'Arleen', 'Milton', 'James', 'Lawrence', 'Edward', 'Susan', 'Patricia', 'Tana', 'Jessica', 'Suzanne', 'Darren', 'Arthur', 'Holly', 'Mary', 'Randal', 'John', 'Laura', 'Betty', 'Chelsea', 'Margaret', 'Angel', 'Jeffrey', 'Mary', 'Donald', 'David', 'Roger', 'Evan', 'Danny', 'William']
    ages  = [17, 58, 79, 8, 10, 57, 4, 98, 19, 47, 81, 68, 48, 13, 39, 21, 98, 51, 49, 12, 24, 78, 36, 59, 3, 87, 94, 85, 43, 69, 15, 52, 57, 36, 52, 5, 52, 5, 33, 10, 71, 28, 70, 9, 25, 28, 76, 71, 22, 35, 35, 100, 9, 95, 69, 52, 66, 91, 39, 84, 65, 29, 20, 98, 30, 83, 30, 15, 88, 89, 24, 98, 62, 94, 86, 63, 34, 23, 23, 19, 10, 80, 88, 67, 17, 91, 85, 97, 29, 7, 34, 38, 92, 29, 14, 52, 94, 62, 70, 22]
    months = ['January', 'March', 'January', 'October', 'April', 'February', 'August', 'January', 'June', 'August', 'February', 'May', 'March', 'June', 'February', 'August', 'June', 'March', 'August', 'April', 'April', 'June', 'April', 'June', 'February', 'September', 'March', 'July', 'September', 'December', 'June', 'June', 'August', 'November', 'April', 'November', 'August', 'June', 'January', 'August', 'May', 'March', 'March', 'March', 'May', 'September', 'August', 'April', 'February', 'April', 'May', 'March', 'March', 'January', 'August', 'October', 'February', 'November', 'August', 'June', 'September', 'September', 'January', 'September', 'July', 'July', 'December', 'June', 'April', 'February', 'August', 'September', 'August', 'February', 'April', 'July', 'May', 'November', 'December', 'February', 'August', 'August', 'September', 'December', 'February', 'March', 'June', 'December', 'February', 'May', 'April', 'July', 'March', 'June', 'December', 'March', 'July', 'May', 'September', 'November']
    people = create_person_objects(names, ages, months)

    # Calls to the two functions you have completed.
    print(get_april_birthdays(people))
    print(get_most_common_month(people))



test()
# Expected result:
# {'Michael': 11, 'Erica': 72, 'Carol': 36, 'Lisa': 37, 'Lawrence': 87, 'Joseph': 25, 'Margaret': 35, 'Andrew': 13, 'Dusty': 53, 'Robert': 89}
# August
```
