# Techniques for Importing Modules
There are other variants of `import` statements that are useful in different situations.

1. To import an individual function or class from a module
   `from module_name import object_name`. For example:
   ```python
   from collections import defaultdict
   defaultdict()
   ```
   Importing individual objects from a module means you only take what you need and you don't need to use the `.` notation.
2. To import multiple individual objects from a module
   `from module_name import first_object, second_object`. For example:
   ```python
   from collections import defaultdict, namedtuple
   ```
   This technique is very common when importing pieces from large libraries.
3. To rename a module
   `import module_name as new_name`. For example:
   ```python
   import multiprocessor as mps
   print(mp.cpu_count())
   ```
   If the name is particularly long or there is a clash with something with the same or similar name, renaming the module can be helpful. Check code examples in the documentation as those will often include a standard abbreviation if one is used for that module. Using an abbreviation that is consistent with others will make your code more readable.
4. To import an object from a module and rename it.
   This can be useful if you have multiple objects with similar names from different packages in your namespace.
   ```python
   from csv import reader as csvreader
   from json import reader as jsonreader
   ```
5. To import every object individually from a module (DO NOT DO THIS)
   `import module_name *`
6. If you really want to use all of the objects from a module, use the standard import module_name statement instead and access each of the objects with the dot notation. `import module_name`

## Modules, Packages, and Names
In order to manage the code better, modules in the Python Standard Library are split down into **sub-modules** that are contained within a package. A **package** is simply a module that contains sub-modules. A sub-module is specified with the usual dot notation.

Modules that are submodules are specified by the package name and then the submodule name separated by a dot. You can import the submodule like this.
`import package_name.submodule_name`. For example:
```python
import os.path
os.path.isdir('my_path')
```
However, this syntax for importing will only works for *submodules*. You cannot import functions from a module in this way `import os.path.isdir`. If you want to use other parts of the `os` module too, you could import `os` instead and everything in the `os.path` will still be available. One more note is:

```python
from datetime import datetime
```
This imports the `datetime` class from the `datetime` module. Note that after this, using `datetime` will refer to the datetime class not the module.
