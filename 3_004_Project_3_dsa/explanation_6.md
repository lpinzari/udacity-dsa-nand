# Max and Min in unsorted array

Since we have no information about the input array order, a natural solution would be to scan the array in a single traversal and maintain the result in two auxiliary variables (**min, max**).

## Time and Space Complexity

In terms of **Time Complexity**, the algorithm takes **O(n)**, where **n** is the size of the input array. The algorithm must explore all the elements in the array and, hence, there is no algorithm that can solve the problem more efficiently than **O(n)**. It follows that the time complexity of this problem is big Omega of n.

To demonstrate this, we compare the execution time of this algorithm to the **min** and **max** functions. The results show that the algorithm's time execution scales proportionally to the output size. These tests are included in the script.

In terms of **Space Complexity**, the algorithm takes constant resources, **O(1)**. The number of auxiliary variables are alway two and, therefore, it does not scale with the size of the input.
