# Search in a rotated sorted array

The logic behind the algorithm is based on the **search** of the **pivot index** in the input array **A**. This index gives the position of the smallest element in **A** and, hence, splits **A** in two subarrays sorted in ascending order. This property is particularly useful as an ordinary binary search can be applied in the two subarrays to find the position of the target value. The two functions that accomplish these tasks are: `rotated_array_pivot(array)` and `binary_search(array, target)`.

## Time and Space Complexity

In terms of **Time Complexity**, the implemented methods take **O(log n)** in the *worst case* (target value is not found), where **n** is the **size** of the array **A**.

The approach employed in the `rotated_array_pivot` is a *variant* of the **binary search** algorithm. The algorithm at each iteration halves the search space by comparing the `mid` value with the first and last element in the subarray. The algorithm stops when the `mid` value is the first element in the sequence (subarray) with the minimum value.
The *worst case* scenario occurs when the minimum value or item is the first element in the array. In this case, the number of iterations (*n -> inf*) is exactly **log<sub>2</sub>(n) +1** when **n = 2<sup>k</sup>**, where **k** is a positive integer and **log<sub>2</sub>(n) + 2** such that **2<sup>k</sup> < n <= 2<sup>k+1</sup>**. As a consequence, the **Time Complexity** of this function is **O(log n)**.
Since finding the pivot and the binary search are all **O(log n)**, the overall time complexity of the algorithm is **O(log n)**.

As for the **Space Complexity**, the algorithm takes constant space resources: **O(1)**. The two implemented functions use iteration to traverse the array **A** and, therefore, do not require extra storage depending on the input size.
