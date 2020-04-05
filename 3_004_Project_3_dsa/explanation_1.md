# Finding the Floor Square Root of an integer

The basic idea of the algorithm is to implement a *variance* of the **binary search** by finding the closest number **s** such that its square is below the input **n** (*i.e* **s<sup>2</sup> <= n < (s+1)<sup>2</sup>** ). The method consists of repeatedly bisecting the initial interval by computing the `middle` point and selecting the subinterval in which the `middle_squared` is bigger or smaller then the given number **n**. For testing the correctness of the implemented algorithm, the `sqrt` and `floor` built-in functions of the Math module have been used.

## Time and Space Complexity

In terms of **Time Complexity** the **binary search** takes **O(log n)**, where **n** represents the input number itself. It's worth noting that the number of iterations in the while loop is exactly **log<sub>2</sub>(n) - 2** when **n** is a perfect square (*i.e* **s<sup>2</sup> = n**), and **log<sub>2</sub>(n) -1** otherwise. It follows that the number of iterations do not depend on a particular instance of the problem and there is no best, average or worst case.

As for the **Space Complexity**, it is independent of the input size as the execution of each iteration in the algorithm requires only the same set of variables. As a consequence, the space complexity is **constant**, **O(1)**.
