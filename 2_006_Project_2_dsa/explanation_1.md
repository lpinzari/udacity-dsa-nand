# Least Recently Used Cache

The *LRU* cache utilizes an internal ***doubly linked list (DLL)*** with two pointers ( *head, tail* ) to maintin the *least-recently-used* structure and a ***hash map*** or ***dictionary*** to retrieve items in the cache.

## Time and Space Complexity
**Time Complexity**:
The use of two pointers in the DLL allows to ***insert*** a new item ( *head* ) and ***remove*** the *least-recently-used* item ( *tail* ) in constant time: ***O(1)*** .
Similarly, the dictionary data structure executes the ***look-up*** operation in ***O(1)*** time.

**Space Complexity**: As in terms of space complexity, the structures require ***O(n)***, where ***n*** is the number of elements in the cache. In the *worst-case* scenario ***n = c***, where ***c*** is the capacity of the cache.
