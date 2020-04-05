
# Building a Trie in Python

Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
* A `Trie` class that contains the root node (empty string)
* A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

Give it a try by implementing the `TrieNode` and `Trie` classes below!


```python
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False 
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie: Check if char is in the dictionary keys
        if char not in self.children:
            self.children[char] = TrieNode()
    
    def find(self, char):
        ## check if char is in this TrieNode
        if char in self.children:
            return True
        return False
    
    def __str__(self):
        ## A description of this TrieNode
        trie_children = self.children
        count_children = len(trie_children)
        desc = ""
        for key,value in trie_children.items():
            if count_children > 1 or count_children == 0:
                desc += str(key) + "=>" + str(value) + "\n"
            else:
                desc += str(key) + "=>" + str(value)
        
        return desc
    
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
    
    def insert(self, word):
        ## Add a word to the Trie 
        current_node = self.root
        
        for char in word:
            # Add a child node in this Trie
            current_node.insert(char)
            # update the iterator to the next node 
            current_node = current_node.children[char]
        # the last node
        current_node.is_word = True
    
    def find(self, prefix):
        ## Find the Trie node that represents this prefix 
        current_node = self.root 
        
        if prefix == '' or prefix is None:
            return None
        
        for char in prefix:

            if not current_node.find(char):
                return None
            
            current_node = current_node.children[char]
            
        return current_node
    
    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root
        
        if word == '' or word is None:
            return None

        for char in word:
            
            if not current_node.find(char):
                return False
            
            current_node = current_node.children[char]

        return current_node.is_word


wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
print(wordList)
word_trie = Trie()

print("\t Test Insert and exists functions\n")
# Add words
for word in wordList:
    word_trie.insert(word)

# Test words
test_words = [
    "ant", "anthology", "antagonist", "antonym", "anth",
    "fun", "function", "factory", "fu",
    "trie", "trigger", "trigonometry", "tripod", "tri"
]

for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))

print("\n\t Test Find prefix function\n")
test_prefixes = ['a', 'an', 'ant', 'anto', 'anth', '', None]
for prefix in test_prefixes:
    prefixNode = word_trie.find(prefix)
    if prefixNode:
        print('"{}" is a prefix \nTrieNode: \n{}'.format(prefix, prefixNode.children.items()))
        print('"{}": \n{}\n'.format(prefix,prefixNode))
    else:
        print('"{}" is not a prefix.\n {}\n'.format(prefix,word_trie.find(prefix)))

```

    ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
    	 Test Insert and exists functions
    
    "ant" is a word.
    "anthology" is a word.
    "antagonist" is a word.
    "antonym" is a word.
    "anth" is not a word.
    "fun" is a word.
    "function" is a word.
    "factory" is a word.
    "fu" is not a word.
    "trie" is a word.
    "trigger" is a word.
    "trigonometry" is a word.
    "tripod" is a word.
    "tri" is not a word.
    
    	 Test Find prefix function
    
    "a" is a prefix 
    TrieNode: 
    dict_items([('n', <__main__.TrieNode object at 0x7f23d59b9048>)])
    "a": 
    n=>t=>h=>o=>l=>o=>g=>y=>
    a=>g=>o=>n=>i=>s=>t=>
    o=>n=>y=>m=>
    
    
    "an" is a prefix 
    TrieNode: 
    dict_items([('t', <__main__.TrieNode object at 0x7f23d59b9d30>)])
    "an": 
    t=>h=>o=>l=>o=>g=>y=>
    a=>g=>o=>n=>i=>s=>t=>
    o=>n=>y=>m=>
    
    
    "ant" is a prefix 
    TrieNode: 
    dict_items([('h', <__main__.TrieNode object at 0x7f23d59b9a58>), ('a', <__main__.TrieNode object at 0x7f23e4333b70>), ('o', <__main__.TrieNode object at 0x7f23d59aef28>)])
    "ant": 
    h=>o=>l=>o=>g=>y=>
    a=>g=>o=>n=>i=>s=>t=>
    o=>n=>y=>m=>
    
    
    "anto" is a prefix 
    TrieNode: 
    dict_items([('n', <__main__.TrieNode object at 0x7f23d59ae358>)])
    "anto": 
    n=>y=>m=>
    
    "anth" is a prefix 
    TrieNode: 
    dict_items([('o', <__main__.TrieNode object at 0x7f23d59b9940>)])
    "anth": 
    o=>l=>o=>g=>y=>
    
    "" is not a prefix.
     None
    
    "None" is not a prefix.
     None
    


# Finding Suffixes

Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.

Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)


```python
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False 
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie: Check if char is in the dictionary keys
        if char not in self.children:
            self.children[char] = TrieNode()
    
    def find(self, char):
        ## check if char is in this TrieNode
        if char in self.children:
            return True
        return False
    
    def __str__(self):
        ## A description of this TrieNode
        trie_children = self.children
        count_children = len(trie_children)
        desc = ""
        for key,value in trie_children.items():
            if count_children > 1 or count_children == 0:
                desc += str(key) + "=>" + str(value) + "\n"
            else:
                desc += str(key) + "=>" + str(value)
        
        return desc    
    
    
    def prefix_words(self, prefix):
        ## Get all the complete words with a given prefix
        trie_children = self.children
        words = []
        if self.is_word:
            words.append(prefix)
        for key,value in trie_children.items():
            words.extend(value.prefix_words(prefix + key))
        return words
    
    def suffixes(self, suffix = ''):
        ## function that collects the suffix for 
        ## all complete words below this point
        prefixes_words = self.prefix_words(suffix)
        
        suffixes = []
        # discard the prefix and get the remaining characters 
        for word in prefixes_words:
            suffixes.append(word[len(suffix):])
        
        return suffixes


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
    
    def insert(self, word):
        ## Add a word to the Trie 
        current_node = self.root
        
        for char in word:
            # Add a child node in this Trie
            current_node.insert(char)
            # update the iterator to the next node 
            current_node = current_node.children[char]
        # the last node
        current_node.is_word = True
    
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        ## Return None if prefix is not found
        
        current_node = self.root 
        
        if prefix == '' or prefix is None:
            return None
        
        for char in prefix:

            if not current_node.find(char):
                return None
            
            current_node = current_node.children[char]
            
        return current_node
    
    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root
        
        if word == '' or word is None:
            return None

        for char in word:
            
            if not current_node.find(char):
                return False
            
            current_node = current_node.children[char]

        return current_node.is_word
```

# Testing it all out

Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.


```python
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Test words
test_words = [
    "ant", "anthology", "antagonist", "antonym", "anth",
    "fun", "function", "factory", "fu",
    "trie", "trigger", "trigonometry", "tripod", "tri"
]
print('Dictionary list: {}'.format(wordList))
print("\n\t Test Insert and exists functions\n")
for word in test_words:
    if MyTrie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))
        
print("\n\t Test find/prefix/suffix function\n")

test_prefixes = ['a', 'an', 'ant', 'anto', 'anth', '', None]
for prefix in test_prefixes:
    prefixNode = MyTrie.find(prefix)
    if prefixNode:
        print('"{}" is a prefix \n'.format(prefix))
        print('TrieNode: \n{}'.format(prefixNode.children.items()))
        print('Words with prefix "{}" : {} '.format(prefix,prefixNode.prefix_words(prefix)))
        print('Auto-complete:')
        print('\n'.join(prefixNode.suffixes()))
        print('\n')
    else:
        print('"{}" is not a prefix.\n {}\n'.format(prefix,prefixNode))

```

    Dictionary list: ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
    
    	 Test Insert and exists functions
    
    "ant" is a word.
    "anthology" is a word.
    "antagonist" is a word.
    "antonym" is a word.
    "anth" is not a word.
    "fun" is a word.
    "function" is a word.
    "factory" is a word.
    "fu" is not a word.
    "trie" is a word.
    "trigger" is a word.
    "trigonometry" is a word.
    "tripod" is a word.
    "tri" is not a word.
    
    	 Test find/prefix/suffix function
    
    "a" is a prefix 
    
    TrieNode: 
    dict_items([('n', <__main__.TrieNode object at 0x7fc60c0bfa90>)])
    Words with prefix "a" : ['ant', 'anthology', 'antagonist', 'antonym'] 
    Auto-complete:
    nt
    nthology
    ntagonist
    ntonym
    
    
    "an" is a prefix 
    
    TrieNode: 
    dict_items([('t', <__main__.TrieNode object at 0x7fc60c0bf5c0>)])
    Words with prefix "an" : ['ant', 'anthology', 'antagonist', 'antonym'] 
    Auto-complete:
    t
    thology
    tagonist
    tonym
    
    
    "ant" is a prefix 
    
    TrieNode: 
    dict_items([('h', <__main__.TrieNode object at 0x7fc60c0bf710>), ('a', <__main__.TrieNode object at 0x7fc60c0bff98>), ('o', <__main__.TrieNode object at 0x7fc60c0bf080>)])
    Words with prefix "ant" : ['ant', 'anthology', 'antagonist', 'antonym'] 
    Auto-complete:
    
    hology
    agonist
    onym
    
    
    "anto" is a prefix 
    
    TrieNode: 
    dict_items([('n', <__main__.TrieNode object at 0x7fc60c0bf208>)])
    Words with prefix "anto" : ['antonym'] 
    Auto-complete:
    nym
    
    
    "anth" is a prefix 
    
    TrieNode: 
    dict_items([('o', <__main__.TrieNode object at 0x7fc60c0bf240>)])
    Words with prefix "anth" : ['anthology'] 
    Auto-complete:
    ology
    
    
    "" is not a prefix.
     None
    
    "None" is not a prefix.
     None
    



```python
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
```


<p>Failed to display Jupyter Widget of type <code>interactive</code>.</p>
<p>
  If you're reading this message in the Jupyter Notebook or JupyterLab Notebook, it may mean
  that the widgets JavaScript is still loading. If this message persists, it
  likely means that the widgets JavaScript library is either not installed or
  not enabled. See the <a href="https://ipywidgets.readthedocs.io/en/stable/user_install.html">Jupyter
  Widgets Documentation</a> for setup instructions.
</p>
<p>
  If you're reading this message in another frontend (for example, a static
  rendering on GitHub or <a href="https://nbviewer.jupyter.org/">NBViewer</a>),
  it may mean that your frontend doesn't currently support widgets.
</p>




```python

```
