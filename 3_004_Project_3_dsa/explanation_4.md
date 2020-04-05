# Dutch National Flag Problem

This problem is a *varaint* of a classical programming exercise popularised by E.W.Dijkstra as the *Dutch National Flag* problem, because it is like sorting an array with three possible key values **{0, 1, 2}** which might correspond to the three colours on the flag {red, white, blue}.

Dijkstra's solution is based on a **single left-to-right** pass through the array **A** that maintains a pointer *lt* (called **low** in the code) to store next position of smaller element from beginning **A[0, ..., lt -1 ]**  is less than **1** (*i.e* zeroes); a pointer *gt* (called **high** in the code) to store next position of greater element from end, **A[gt + 1, ..., end]** is greater than **1** (*i.e* twos); and a pointer *i* (called **mid** in the code) such that **A[lt, ... , i-1]** are equal to one and **A[i, ... , gt]** are not yet examined.

## Time and Space Complexity

In terms of **Time Complexity**, the algorithm takes **O(n)**, where **n** is the size of the array. At each iteration of the algorithm the unknown region is shrunk by examining **A[mid]** and moving the left or right pointers, forward or backward. These tasks require only **O(1)**, resulting in an overall complexity of **O(n)**.

As for the **Space Complexity**, this algorithm is *in-place*, meaning that we do not need auxiliary data structures (only three pointers to swap the elements in the array) that depends on the input size, resulting, therefore, in **O(1)**.
