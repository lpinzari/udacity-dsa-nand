# Autocomplete with Trie

A **Trie** is a tree-like data structure whose nodes store letters of an alphabet. By structuring the nodes in a particular way, words and strings can be retrieved from the structure by traversing down a branch path of the tree.

One way implementing **Trie** is linked set of nodes, where each node (**TrieNode**) contains just two things:

1. A boolean value to mark the last node of every key as end of word node (**is_word** in the code).

2. A Hash map (dictionary) to store children of a node. Python's dictionaries are dynamic, so a given node can have a variable number of children and, hence, it allocates memory only for alphabet in use. Following this approach, we do not waste space storing null pointers in a data structures designed to accomodate only a fixed number of keys, like an array of 26 elements that represent the entire alphabet.

The basic operations implemented for the **Trie** are:

- `insert(word)`: Add a word to the Trie
- `find(prefix)`: Find the TrieNode that represent this prefix  

The autocomplete functionality has been implemented in `suffixes(suffix)` function. The suffixes function is responsible for getting the suffix of that prefix, that is the remaining characters of the complete words lying in the trie below that node. This function calls a supporting recursive function in the **TrieNode** class. The recursive procedure returns a list of all the complete words with a given prefix. The returned list is then traversed and the first letters composing the prefix are removed.

## Time and Space Complexity

Let's look at the Big O **Time Complexity**. The time of inserting and any searching operation depends on the length of the word **l** and the total number of words **n**. The runtime of these operations depends, therefore, on how many words the Trie contains, and how long they might potentially be. It follows that the time complexity is **O(l * n)**, where **l** is the longest word and **n** is the total number of words.

In terms of **Space Complexity**, the space used with every node is proportional to number of children. In the worst case scenario the number of children is equal to the entire ALPHABET, resulting in a complete n-ary tree. It follows that the space required is **O((ALPHABET_SIZE)<sup>(l+1)</sup> -1)**. For example, in a binary tree each node has two children and the total number of nodes is **2<sup>h</sup> -1**. In this case, ALPHABET_SIZE is 2 **{0,1}** and **h=l+1**.
