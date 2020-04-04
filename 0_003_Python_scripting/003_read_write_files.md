# Reading and Writing Files

To follow along with the example above, create a new file in Atom, copy the following text into it, and save it as **my_file.txt**!

**my_file.txt**
```console
Hello!!

You've read the contents of this file!
```

Here's how we read and write files in Python.

**Reading a File**

**demo.py**
```python
f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()
print(file_data)
```

Output:
```console
$ python demo.py
Hello!!

You've read the contents of this file!
```

1. First open the file using the built-in function, `open`. This requires a string that shows the path to the file. The `open` function returns a file object, which is a Python object through which Python interacts with the file itself. Here, we assign this object to the variable `f`.
2. There are optional parameters you can specify in the `open` function. One is the mode in which we open the file. Here, we use `r` or read only. This is actually the **default value** for the mode argument.
3. Use the read method to access the contents from the file object. This read method takes the text contained in a file and puts it into a string. Here, we assign the string returned from this method into the variable `file_data`.
4. When finished with the file, use the `close` method to free up any system resources taken up by the file.

**Writing to a File**

```python
f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()
```
1. Open the file in writing ('`w`') mode. If the file does not exist, Python will create it for you. If you open an existing file in writing mode, any content that it had contained previously will be deleted. If you're interested in adding to an existing file, without deleting its content, you should use the append ('`a`') mode instead of write.
2. Use the write method to add text to the file.
3. Close the file when finished.

## Too Many Open Files
Run the following script in Python to see what happens when you open too many files without closing them!

```python
files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))
    print(i)
```

*run the script*

```console
$ python demo.py
1
2
.
.
7163
7164
Traceback(most recent call last):
  File "demo.py", line 3, in <module>
OSError: [Errno 24] too many open files: 'some_file.txt'
```

If we open a lot of files without closing them, we can run out of **file handles** and we won't be able to open any new files. Exactly how many files you can open before running out of handles will depend on your operating system. At some point for a large enough number, you will receive an error. We can see that at `7164` open files, the system no longer had available resources to open any new files. To avoid this, it is always a good idea to close any file you no longer need. Opening a file object is like opening a window that's only one character wide and it always starts off at the very start of the file. Think instead of the file as a **long stream of characters**. The file object can look at just one character at a time in order.

## With
Python provides a special syntax that auto-closes a file for you once you're finished using it.

```python
with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()
print(file_data)
```

This ```with``` keyword allows you to open a file, do operations on it, and automatically close it after the indented code is executed, in this case, reading from the file. Now, we don’t have to call f.close()! You can only access the file object, f, within this indented block.

The code `as f:` assigns the file object created by the `open` function to the variable named `f`. The first line of code is basically this line of code `f = open('my_path/my_file.txt', 'r')` except you can only access the object `f` within the `with` block. This is another kind of scope. Once you leave the indented block, the file is closed and you are no longer able to interact with it. For example, trying to call `file_data = f.read()` outside the block would return an error. However, just because you closed the file doesn't mean you lose the data. In the example above, we read in the file in the second line and get the file data string that has the text contained in the file. Calling `file_data` outside the block works fine. We can use all the usual string methods on this file data string to process its contents.

## Calling the read Method with an Integer
In the code you saw earlier, the call to `f.read()` had no arguments passed to it. This defaults to reading all the remainder of the file from its current position - the whole file. If you pass the read method an integer argument, it will read up to that number of characters, output all of them, and keep the 'window' at that position ready to read on.

Let's see this in an example that uses the following file, *camelot.txt*:

```console
We're the knights of the round table
We dance whenever we're able
```

Here's a script that reads in the file a little at a time by passing an integer argument to .`read()`.

```python
with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())
```
Outputs:

```console
We
're the
knights of the round table
We dance whenever we're able
```

Each time we called `read` on the file with an integer argument, it read up to that number of characters, outputted them, and kept the 'window' at that position for the next call to `read`. This makes moving around in the open file a little tricky, as there aren't many landmarks to navigate by.

## Reading Line by Line
\n s in blocks of text are newline characters. The newline character marks the end of a line, and tells a program (such as a text editor) to go down to the next line. However, looking at the stream of characters in the file, \n is just another character.

Fortunately, Python knows that these are special characters and you can ask it to read one line at a time. See the Python [documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) to use the method `readline()`.

Conveniently, Python will loop over the lines of a file using the syntax `for line in file`. I can use this to create a list of lines in the file. Because each line still has its newline character attached, I remove this using `.strip()`.

```python
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)
```

Outputs:

```console
["We're the knights of the round table", "We dance whenever we're able"]
```

**Quiz: Flying Circus Cast List**
You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

Write a function called `create_cast_list` that takes a filename as input and returns a list of actors' names. It will be run on the file `flying_circus_cast.txt` (this information was collected from imdb.com). Each line of that file consists of an actor's name, a comma, and then some (messy) information about roles they played in the programme. You'll need to extract only the name and add it to a list. You might use the `.split()` [method](https://docs.python.org/3/library/stdtypes.html#str.split) to process each line.

**flying_circus_cast.txt**

```console
Graham Chapman,  Various / ... (46 episodes, 1969-1974)
Eric Idle,  Various / ... (46 episodes, 1969-1974)
Terry Jones,  Various / ... (46 episodes, 1969-1974)
Michael Palin,  It's Man / ... (46 episodes, 1969-1974)
Terry Gilliam,  Various / ... (46 episodes, 1969-1974)
John Cleese,  Announcer / ... (40 episodes, 1969-1973)
Carol Cleveland,  Various / ... (34 episodes, 1969-1974)
Ian Davidson,  Algy Braithwaite / ... (8 episodes, 1969-1970)
```

```python
def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
```

Output:

```console
Graham Chapman
Eric Idle
Terry Jones
Michael Palin
Terry Gilliam
John Cleese
Carol Cleveland
Ian Davidson
```
