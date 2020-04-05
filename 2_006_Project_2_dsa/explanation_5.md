# Blockchain

A **Blockchain** is a sequential chain of records, similar to a **linked list**. For this problem, we implemented a class **Blockchain**.

The **BlockChain** class uses a class variable to keep track of the list **size** and a **reference** (**tail**) to the last node of the list. Each node in the list is modelled by a **Block** class, which store: a *real-time timestamp*, a text string as *data*, a *previous hash_code*, a *reference to the previous block* and a *SHA-256 hash code* of the *timestamp*, *data* and *previous_hash* fields.

The **BlockChain** class implements the following methods: `append(value)`, `get_size()`, `to_list()`, `print_chain()`.

## Time and Space Complexity

Let **n** be the number of nodes or blocks in the **BlockChain** class. Then, the **Time Complexity** of the implemented methods is:

- `append(value)`: **O(1)**
- `get_size()`: **O(1)**
- `to_list()`: **O(n)**
- `print_chain()`: **O(n)**

As for the **Space Complexity**, being a linked list in its core structure, it has **O(n)**.
