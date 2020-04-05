# Finding Files

The underlying data structure of a File system is actually a tree where files act as *leaves* and directories act as *internal nodes*. The algorithm implementation is basically a **depth-first-search** that traverses the entire tree. For each *directory* (*internal nodes*), we keep the files that match the desired *extension* and visit the *sub-directories* by calling the subsequent calls to the function.

## Time and Space Complexity

In terms of ***Time Complexity***, the algorithm depends on the *height* (**h**) and the  number of leaves (files) in the tree (***n***). The  **h** of a tree is defined as the number of edges on the longest path from the root to a leaf (i.e depth of its deepest node), and therefore is proportional to the number of directories (***d***). Assuming that all the leaves in the tree are files, we can imagine all directories being nested as the worst case the resulting time complexity is ***O(n∙d)***.

As in terms of ***Space Complexity***, the structure requires ***O(n+d)***, where ***n*** is the number of files with the desired extension and ***d*** is the number of directories.

Each recursive call of the `find_files()` function creates its own stack frame in memory, tacking up space on the call stack. Secondly, each stack frame contains local variables.
We can approximate the stack frames by analyzing how many times the function `find_files()` will be called (call_stack_space) and the number of returns the function does (returned_list_space).

As for the call_stack_space, the function is only called every time the node visited is a directory, so the number of calls is directly proportional to the number of directories in the tree. In terms of returned_list_space, in the worst case the list will contain all filenames in the tree and that will occupy space.
