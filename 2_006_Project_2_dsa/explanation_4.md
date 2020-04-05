# Active Directory

The algorithm explores recursively the subgroups and users in the *Active Directory*. The algorithm follows the same logic discussed in the *explanation_2.md* for the Finding files problem.

## Time and Space Complexity


The **Time Complexity** in the worst case scenario is ***O(g·u)***, where **g** is the number of groups and **u** the number of users. In this case the user is not in the Active Directory and hence the algorithm must explore all the subgroups and for each subgroup all the users in that subgroup, resulting in ***O(g·u)***.

As in terms of ***Space Complexity***, similar to problem 2, the structure requires ***O(g + u)***. We can imagine all groups being nested as the worst case for the call stack space and, therefore, the number of recursive calls will be ***g***. For the auxiliary lists space, worst case is when all users and groups are hold in memory before the call stack starts popping back to the root node.
