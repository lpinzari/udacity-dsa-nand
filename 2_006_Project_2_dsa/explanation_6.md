# Union and Intersection of Two linked lists

Task: You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.

For the **union** and **intersection** problems, the approach has been to use ***three iterators*** to loop over the three linked lists and auxiliaries ***Python's sets*** data structure.

In the **union** implementation, the basic idea is to iterate over the two inputs linked list and add the elements in a Python's set. Lastly, we iterate over the resulting set to build the new linked list.

In the **intersection** implementation, the first step is to convert the two linked lists to two sets. Lastly, we compare the common elements in both sets and put it in a new linked list. This can be achieved by iterating through one set and checking the presence of each element in the other set.


## Time and Space Complexity

Let **s** and **t** be the length of the first and second list, respectively. (i.e **s = len(llist_1) ;  t = len(llist_2)**.

In terms of **Time Complexity**, the number of iterations are exactly equal to the number of elements in the two linked lists. It follows that this algorithm is **Theta(s + t)** (i.e worst, average and best case are identical).

- `union(llist_1, llist_2)`: **O( s + t )**
- `intersection(llist_1, llist_2)`: **O( s + t )**

In terms of **Space Complexity**, both functions require **O(s + t)**; in the worst case when all elements in the lists are different. Take note that if all elements are unique, then you will end up with an empty intersection list. But the auxiliaries sets used to convert the input lists will still occupy space and, therefore, is proportional to `s + t`.
