
# Longest Palindromic Subsequence

In this notebook, you'll be tasked with finding the length of the *Longest Palindromic Subsequence* (LPS) given a string of characters.

As an example:
* With an input string, `ABBDBCACB`
* The LPS is `BCACB`, which has `length = 5`

In this notebook, we'll focus on finding an optimal solution to the LPS task, using dynamic programming. There will be some similarities to the Longest Common Subsequence (LCS) task, which is outlined in detail in a previous notebook. It is recommended that you start with that notebook before trying out this task.

### Hint
**Storing pre-computed values**

The LPS algorithm depends on looking at one string and comparing letters to one another. Similar to how you compared two strings in the LCS (Longest Common Subsequence) task, you can compare the characters in just *one* string with one another, using a matrix to store the results of matching characters.


For a string on length n characters, you can create an `n x n` matrix to store the solution to subproblems. In this case, the subproblem is the length of the longest palindromic subsequence, up to a certain point in the string (up to the end of a certain substring).

It may be helpful to try filling up a matrix on paper before you start your code solution. If you get stuck with this task, you may look at some example matrices below (see the section titled **Example matrices**), before consulting the complete solution code.



```python
# imports for printing a matrix, nicely
import pprint
pp = pprint.PrettyPrinter()

def lps(input_string): 
    
    # TODO: Complete this implementation of the LPS function
    # The function should return one value: the LPS length for the given input string
    n = len(input_string) 
  
    # create a lookup table to store results of subproblems (n x n matrix with zeros)
    L = [[0 for x in range(n)] for x in range(n)] 
  
    # strings of length 1 have LPS length = 1 (main diagonal ones) Base case
    for i in range(n): 
        L[i][i] = 1 
    print('\t {}'.format(input_string))
    pp.pprint(L)
    # consider all substrings
    for s_size in range(2, n+1):
        print('s_size: {}'.format(s_size))
        for start_idx in range(n+1 - s_size):
            end_idx = start_idx + s_size - 1
            print('\t (start_idx, end_idx): ({},{}) \t {}'.format(start_idx, end_idx,input_string[start_idx:end_idx+1]), end = "")
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2 (Base case)
                L[start_idx][end_idx] = 2
                print(' match: L[{}][{}] = 2'.format(start_index,end_index))
            elif input_string[start_idx] == input_string[end_idx]: 
                # general match case
                # add two more characthers to the the solution of the subproblem
                L[start_idx][end_idx] = L[start_idx+1][end_idx-1] + 2
                print(' match: L[{}][{}] = L[{}][{}] + 2'.format(start_idx,end_idx,start_idx+1,end_idx-1))
            else:
                # no match case, taking the max of two values
                L[start_idx][end_idx] = max(L[start_idx][end_idx-1], L[start_idx+1][end_idx])
                print(' no match: L[{}][{}] = max(L[{}][{}], L[{}][{}])'.format(start_idx,end_idx,start_idx,end_idx+1,start_idx+1,end_idx))
        pp.pprint(L)
    # debug line
    #pp.pprint(L)
    
    return L[0][n-1] # value in top right corner of matrix

```


```python
def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
```


```python
string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)
```

    	 TACOCAT
    [[1, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1]]
    s_size: 2
    	 (start_idx, end_idx): (0,1) 	 TA no match: L[0][1] = max(L[0][2], L[1][1])
    	 (start_idx, end_idx): (1,2) 	 AC no match: L[1][2] = max(L[1][3], L[2][2])
    	 (start_idx, end_idx): (2,3) 	 CO no match: L[2][3] = max(L[2][4], L[3][3])
    	 (start_idx, end_idx): (3,4) 	 OC no match: L[3][4] = max(L[3][5], L[4][4])
    	 (start_idx, end_idx): (4,5) 	 CA no match: L[4][5] = max(L[4][6], L[5][5])
    	 (start_idx, end_idx): (5,6) 	 AT no match: L[5][6] = max(L[5][7], L[6][6])
    [[1, 1, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 1]]
    s_size: 3
    	 (start_idx, end_idx): (0,2) 	 TAC no match: L[0][2] = max(L[0][3], L[1][2])
    	 (start_idx, end_idx): (1,3) 	 ACO no match: L[1][3] = max(L[1][4], L[2][3])
    	 (start_idx, end_idx): (2,4) 	 COC match: L[2][4] = L[3][3] + 2
    	 (start_idx, end_idx): (3,5) 	 OCA no match: L[3][5] = max(L[3][6], L[4][5])
    	 (start_idx, end_idx): (4,6) 	 CAT no match: L[4][6] = max(L[4][7], L[5][6])
    [[1, 1, 1, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 0, 0],
     [0, 0, 1, 1, 3, 0, 0],
     [0, 0, 0, 1, 1, 1, 0],
     [0, 0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 1]]
    s_size: 4
    	 (start_idx, end_idx): (0,3) 	 TACO no match: L[0][3] = max(L[0][4], L[1][3])
    	 (start_idx, end_idx): (1,4) 	 ACOC no match: L[1][4] = max(L[1][5], L[2][4])
    	 (start_idx, end_idx): (2,5) 	 COCA no match: L[2][5] = max(L[2][6], L[3][5])
    	 (start_idx, end_idx): (3,6) 	 OCAT no match: L[3][6] = max(L[3][7], L[4][6])
    [[1, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 1, 3, 0, 0],
     [0, 0, 1, 1, 3, 3, 0],
     [0, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 1]]
    s_size: 5
    	 (start_idx, end_idx): (0,4) 	 TACOC no match: L[0][4] = max(L[0][5], L[1][4])
    	 (start_idx, end_idx): (1,5) 	 ACOCA match: L[1][5] = L[2][4] + 2
    	 (start_idx, end_idx): (2,6) 	 COCAT no match: L[2][6] = max(L[2][7], L[3][6])
    [[1, 1, 1, 1, 3, 0, 0],
     [0, 1, 1, 1, 3, 5, 0],
     [0, 0, 1, 1, 3, 3, 3],
     [0, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 1]]
    s_size: 6
    	 (start_idx, end_idx): (0,5) 	 TACOCA no match: L[0][5] = max(L[0][6], L[1][5])
    	 (start_idx, end_idx): (1,6) 	 ACOCAT no match: L[1][6] = max(L[1][7], L[2][6])
    [[1, 1, 1, 1, 3, 5, 0],
     [0, 1, 1, 1, 3, 5, 5],
     [0, 0, 1, 1, 3, 3, 3],
     [0, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 1]]
    s_size: 7
    	 (start_idx, end_idx): (0,6) 	 TACOCAT match: L[0][6] = L[1][5] + 2
    [[1, 1, 1, 1, 3, 5, 7],
     [0, 1, 1, 1, 3, 5, 5],
     [0, 0, 1, 1, 3, 3, 3],
     [0, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 1]]
    7
    Pass



```python
string = 'BANANA'
solution = 5
test_case = [string, solution]
test_function(test_case)
```

    	 BANANA
    [[1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1]]
    s_size: 2
    	 (start_idx, end_idx): (0,1) 	 BA no match: L[0][1] = max(L[0][2], L[1][1])
    	 (start_idx, end_idx): (1,2) 	 AN no match: L[1][2] = max(L[1][3], L[2][2])
    	 (start_idx, end_idx): (2,3) 	 NA no match: L[2][3] = max(L[2][4], L[3][3])
    	 (start_idx, end_idx): (3,4) 	 AN no match: L[3][4] = max(L[3][5], L[4][4])
    	 (start_idx, end_idx): (4,5) 	 NA no match: L[4][5] = max(L[4][6], L[5][5])
    [[1, 1, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
    s_size: 3
    	 (start_idx, end_idx): (0,2) 	 BAN no match: L[0][2] = max(L[0][3], L[1][2])
    	 (start_idx, end_idx): (1,3) 	 ANA match: L[1][3] = L[2][2] + 2
    	 (start_idx, end_idx): (2,4) 	 NAN match: L[2][4] = L[3][3] + 2
    	 (start_idx, end_idx): (3,5) 	 ANA match: L[3][5] = L[4][4] + 2
    [[1, 1, 1, 0, 0, 0],
     [0, 1, 1, 3, 0, 0],
     [0, 0, 1, 1, 3, 0],
     [0, 0, 0, 1, 1, 3],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
    s_size: 4
    	 (start_idx, end_idx): (0,3) 	 BANA no match: L[0][3] = max(L[0][4], L[1][3])
    	 (start_idx, end_idx): (1,4) 	 ANAN no match: L[1][4] = max(L[1][5], L[2][4])
    	 (start_idx, end_idx): (2,5) 	 NANA no match: L[2][5] = max(L[2][6], L[3][5])
    [[1, 1, 1, 3, 0, 0],
     [0, 1, 1, 3, 3, 0],
     [0, 0, 1, 1, 3, 3],
     [0, 0, 0, 1, 1, 3],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
    s_size: 5
    	 (start_idx, end_idx): (0,4) 	 BANAN no match: L[0][4] = max(L[0][5], L[1][4])
    	 (start_idx, end_idx): (1,5) 	 ANANA match: L[1][5] = L[2][4] + 2
    [[1, 1, 1, 3, 3, 0],
     [0, 1, 1, 3, 3, 5],
     [0, 0, 1, 1, 3, 3],
     [0, 0, 0, 1, 1, 3],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
    s_size: 6
    	 (start_idx, end_idx): (0,5) 	 BANANA no match: L[0][5] = max(L[0][6], L[1][5])
    [[1, 1, 1, 3, 3, 5],
     [0, 1, 1, 3, 3, 5],
     [0, 0, 1, 1, 3, 3],
     [0, 0, 0, 1, 1, 3],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
    5
    Pass



```python
string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)
```

    	 BANANO
    [[1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1]]
    s_size: 2
    	 (start_idx, end_idx): (0,1) 	 BA no match: L[0][1] = max(L[0][2], L[1][1])
    	 (start_idx, end_idx): (1,2) 	 AN no match: L[1][2] = max(L[1][3], L[2][2])
    	 (start_idx, end_idx): (2,3) 	 NA no match: L[2][3] = max(L[2][4], L[3][3])
    	 (start_idx, end_idx): (3,4) 	 AN no match: L[3][4] = max(L[3][5], L[4][4])
    	 (start_idx, end_idx): (4,5) 	 NO no match: L[4][5] = max(L[4][6], L[5][5])
    [[1, 1, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
    s_size: 3
    	 (start_idx, end_idx): (0,2) 	 BAN no match: L[0][2] = max(L[0][3], L[1][2])
    	 (start_idx, end_idx): (1,3) 	 ANA match: L[1][3] = L[2][2] + 2
    	 (start_idx, end_idx): (2,4) 	 NAN match: L[2][4] = L[3][3] + 2
    	 (start_idx, end_idx): (3,5) 	 ANO no match: L[3][5] = max(L[3][6], L[4][5])
    [[1, 1, 1, 0, 0, 0],
     [0, 1, 1, 3, 0, 0],
     [0, 0, 1, 1, 3, 0],
     [0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
    s_size: 4
    	 (start_idx, end_idx): (0,3) 	 BANA no match: L[0][3] = max(L[0][4], L[1][3])
    	 (start_idx, end_idx): (1,4) 	 ANAN no match: L[1][4] = max(L[1][5], L[2][4])
    	 (start_idx, end_idx): (2,5) 	 NANO no match: L[2][5] = max(L[2][6], L[3][5])
    [[1, 1, 1, 3, 0, 0],
     [0, 1, 1, 3, 3, 0],
     [0, 0, 1, 1, 3, 3],
     [0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
    s_size: 5
    	 (start_idx, end_idx): (0,4) 	 BANAN no match: L[0][4] = max(L[0][5], L[1][4])
    	 (start_idx, end_idx): (1,5) 	 ANANO no match: L[1][5] = max(L[1][6], L[2][5])
    [[1, 1, 1, 3, 3, 0],
     [0, 1, 1, 3, 3, 3],
     [0, 0, 1, 1, 3, 3],
     [0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
    s_size: 6
    	 (start_idx, end_idx): (0,5) 	 BANANO no match: L[0][5] = max(L[0][6], L[1][5])
    [[1, 1, 1, 3, 3, 3],
     [0, 1, 1, 3, 3, 3],
     [0, 0, 1, 1, 3, 3],
     [0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
    3
    Pass


### Example matrices

Example LPS Subproblem matrix 1:

```
input_string = 'BANANO'

LPS subproblem matrix:
  
     B  A  N  A  N  O
B  [[1, 1, 1, 3, 3, 3],
A   [0, 1, 1, 3, 3, 3],
N   [0, 0, 1, 1, 3, 3],
A   [0, 0, 0, 1, 1, 1],
N   [0, 0, 0, 0, 1, 1],
O   [0, 0, 0, 0, 0, 1]]

LPS length:  3
```

Example LPS Subproblem matrix 2:
```
input_string = 'TACOCAT'

LPS subproblem matrix:

     T  A  C  O  C  A  T
T  [[1, 1, 1, 1, 3, 5, 7],
A   [0, 1, 1, 1, 3, 5, 5],
C   [0, 0, 1, 1, 3, 3, 3],
O   [0, 0, 0, 1, 1, 1, 1],
C   [0, 0, 0, 0, 1, 1, 1],
A   [0, 0, 0, 0, 0, 1, 1],
T   [0, 0, 0, 0, 0, 0, 1]]

LPS length:  7
```

Note: The lower diagonal values will remain 0 in all cases.

### The matrix rules

You can efficiently fill up this matrix one cell at a time. Each grid cell only depends on the values in the grid cells that are directly on bottom and to the left of it, or on the diagonal/bottom-left. The rules are as follows:
* Start with an `n x n ` matrix where n is the number of characters in a given string; the diagonal should all have the value 1 for the base case, the rest can be zeros.
* As you traverse your string:
    * If there is a match, fill that grid cell with the value to the bottom-left of that cell *plus* two.
    * If there is not a match, take the *maximum* value from either directly to the left or the bottom cell, and carry that value over to the non-match cell.
* After completely filling the matrix, **the top-right cell will hold the final LPS length**.


```python
## Solution

# imports for printing a matrix, nicely
import pprint
pp = pprint.PrettyPrinter()

# complete LPS solution
def lps(input_string): 
    n = len(input_string) 
  
    # create a lookup table to store results of subproblems 
    L = [[0 for x in range(n)] for x in range(n)] 
  
    # strings of length 1 have LPS length = 1
    for i in range(n): 
        L[i][i] = 1 
    
    # consider all substrings
    for s_size in range(2, n+1): 
        for start_idx in range(n-s_size+1): 
            end_idx = start_idx + s_size - 1
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2
                L[start_idx][end_idx] = 2
            elif input_string[start_idx] == input_string[end_idx]: 
                # general match case
                L[start_idx][end_idx] = L[start_idx+1][end_idx-1] + 2
            else:
                # no match case, taking the max of two values
                L[start_idx][end_idx] = max(L[start_idx][end_idx-1], L[start_idx+1][end_idx]); 
  
    # debug line
    # pp.pprint(L)
    
    return L[0][n-1] # value in top right corner of matrix
```

<span class="graffiti-highlight graffiti-id_d28fhk7-id_3yrlf09"><i></i><button>Show Solution</button></span>

### Complexity

What was the complexity of this?

In the solution, we are looping over the elements of our `input_string` using two `for` loops; these are each of $O(N)$ and nested this becomes $O(N^2)$. This behavior dominates our optimized solution.
