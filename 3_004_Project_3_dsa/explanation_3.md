# Find Two Numbers with Maximum Sum formed by Array Digits

Given an array of integers between **0 to 9**, find two numbers with maximum sum formed by using all digits of the array. The difference in number of digits of the two numbers should be +1, -1. For example:

- Input: [4, 6, 2, 7, 9, 8], [9, 2, 5, 6, 0, 4]
- Output: The two numbers with maximum sum are 952 and 640.

We know that a maximum number can be formed from given digits (0-9) when the largest digit appears first, second largest digit appears second, and so on ... . Finally, the smallest digit appears in the end.

We can extend the same logic to solve this problem. We start by sorting the specified array in ascending order and construct two numbers (say **num1** and **num2**) by picking alternating digits from the array and accumulating the sum in decimal base (*i.e* **num1** is filled with digits at the odd indices and **num2** is filled with digits at the even indices of the sorted array). These tasks can be accomplished by implementing a **mergesort** and a **for loop** to iterate through the sorted array.

## Time and Space Complexity

In terms of **Time Complexity** the algorithm takes **O(n log n)**, where **n** is the size of the input array. Since the **mergesort** always divides the array into two halves and takes linear time to merge two halves, it does not depend on the initial order of the elements in the array and its time complexity is always **O(n log n)** (Big Theta to be precise). Finally, looping through the array takes linear time, resulting in an overall time complexity of **O(n log n)**.

As for the **Space Complexity**, the algorithm takes **O(n)** resources, where **n** is the size of the array. The **mergesort** algorithm is recursive, so it requires **O(log n)** stack space, but the array also allocates an additional **O(n)** space, which dominates the **O(log n)** space required for the stack.
