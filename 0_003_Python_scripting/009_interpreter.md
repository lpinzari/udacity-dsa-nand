# Experimenting With An Interpreter
Start your Python interactive interpreter by entering the command python in your terminal. You can type here to interact with Python directly. This is an awesome place to experiment and try bits of Python code at a time. Just enter Python code, and the output will appear on the next line.

```script
$ python
>>> type(5.23)
<class 'float'>
```
In the interpreter, the value of the last line in a prompt will be outputted automatically. If you had multiple lines where you’d want to output values, you’d still have to use print.

If you start to define a function you will see a change in the prompt, to signify that this is a continuation line. You'll have to include your own indentation as you define the function.

```script
>>> def cylinder_volume(height, radius):
...         pi = 3.14159
...         return height * pi * radius ** 2
```

A drawback of the interpreter is that it’s tricky to edit code. If you made a mistake when typing this function, or forgot to indent the body of the function, you can't use the mouse to click your cursor where you want it. You have to navigate with arrow keys to move the cursor forwards and backwards through the line itself for editing. It would be helpful for you to learn useful shortcuts for actions like moving to the beginning or end of the line.

Notice I can reference any objects I defined earlier in the interpreter!

```script
>>> cylinder_volume(10, 3)
282.7431
```
One useful trick is using the up and down arrow to cycle through your recent commands at the interactive prompt. This can be useful to re-run or adapt code you've already tried.

To quit the Python interactive interpreter, use the command `exit()` or hit `ctrl-D` on mac or linux, and `ctrl-Z` then `Enter` for windows.

IPython
There is actually an awesome alternative to the default Python interactive interpreter, [IPython](https://ipython.org/ipython-doc/3/interactive/tutorial.html), which comes with many additional features.

- tab completion
- ? for details about an object
- ! to execute system shell commands
- syntax highlighting!
