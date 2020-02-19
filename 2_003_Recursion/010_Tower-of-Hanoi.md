
### Problem Statement

The Tower of Hanoi is a puzzle where we have three rods and `n` disks. The three rods are:
    1. source
    2. destination
    3. auxiliary

Initally, all the `n` disks are present on the source rod. The final objective of the puzzle is to move all disks from the source rod to the destination rod using the auxiliary rod. However, there are some rules according to which this has to be done:
    1. Only one disk can be moved at a time.
    2. A disk can be moved only if it is on the top of a rod.
    3. No disk can be placed on the top of a smaller disk.
    
You will be given the number of disks `num_disks` as the input parameter. 

For example, if you have `num_disks = 3`, then the disks should be moved as follows:
    
        1. move disk from source to auxiliary
        2. move disk from source to destination
        3. move disk from auxiliary to destination
        
You must print these steps as follows:    

        S A
        S D
        A D
        
Where S = source, D = destination, A = auxiliary



```python
def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    pass
```

<span class="graffiti-highlight graffiti-id_rh9jy5w-id_aaedpt9"><i></i><button>Hide Solution</button></span>


```python
# Solution
def tower_of_Hanoi_soln(num_disks, source, auxiliary, destination):
    
    if num_disks == 0:
        return
    
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return
    
    tower_of_Hanoi_soln(num_disks - 1, source, destination, auxiliary)
    print("{} {}".format(source, destination))
    tower_of_Hanoi_soln(num_disks - 1, auxiliary, source, destination)
    
def tower_of_Hanoi(num_disks):
    tower_of_Hanoi_soln(num_disks, 'S', 'A', 'D')

tower_of_Hanoi(2)
print('number of disks: 3')
tower_of_Hanoi(3)
print('number of disks: 4')
tower_of_Hanoi(4)
```

    S A
    S D
    A D
    number of disks: 3
    S D
    S A
    D A
    S D
    A S
    A D
    S D
    number of disks: 4
    S A
    S D
    A D
    S A
    D S
    D A
    S A
    S D
    A D
    A S
    D S
    A D
    S A
    S D
    A D


#### Compare your results with the following test cases
* num_disks = 2

        solution 
                S A
                S D
                A D
                
* num_disks = 3

        solution 
                S D
                S A
                D A
                S D
                A S
                A D
                S D

* num_disks = 4
    
        solution
                S A
                S D
                A D
                S A
                D S
                D A
                S A
                S D
                A D
                A S
                D S
                A D
                S A
                S D
                A D
