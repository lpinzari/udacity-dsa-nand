
## Building a Stack in Python

Before we start let us reiterate they key components of a stack. A stack is a data structure that consists of two main operations: push and pop. A push is when you add an element to the **top of the stack** and a pop is when you remove an element from **the top of the stack**. Python 3.x conviently allows us to demonstate this functionality with a list. When you have a list such as [2,4,5,6] you can decide which end of the list is the bottom and the top of the stack respectivley. Once you decide that, you can use the append, pop or insert function to simulate a stack. We will choose the first element to be the bottom of our stack and therefore be using the append and pop functions to simulate it. Give it a try by implementing the function below!

#### Try Building a Stack


```python
class Stack:
    def __init__(self):
         # TODO: Initialize the Stack
    
    def size(self):
         # TODO: Check the size of the Stack
    
    def push(self, item):
         # TODO: Push item onto Stack

    def pop(self):
         # TODO: Pop item off of the Stack
```

#### Test the Stack


```python
MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-161b6dd35e6f> in <module>()
    ----> 1 MyStack = Stack()
          2 
          3 MyStack.push("Web Page 1")
          4 MyStack.push("Web Page 2")
          5 MyStack.push("Web Page 3")


    NameError: name 'Stack' is not defined


<span class="graffiti-highlight graffiti-id_3l78doc-id_l2kcjcz"><i></i><button>Hide Solution</button></span>


```python
# Solution

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()
        
MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")# Solution

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()
        
MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")# Solution

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()
        
MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")

```

    ['Web Page 1', 'Web Page 2', 'Web Page 3']
    Pass
    Pass
    ['Web Page 1', 'Web Page 2', 'Web Page 3']
    Pass
    Pass
    ['Web Page 1', 'Web Page 2', 'Web Page 3']
    Pass
    Pass



```python

```
