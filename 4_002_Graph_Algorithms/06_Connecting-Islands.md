
### Problem Statements

In an ocean, there are `n` islands some of which are connected via bridges. Travelling over a bridge has some cost attaced with it. Find bridges in such a way that all islands are connected with minimum cost of travelling. 

You can assume that there is at least one possible way in which all islands are connected with each other. 

You will be provided with two input parameters:
    
1. `num_islands` = number of islands
    
2. `bridge_config` = list of lists. 
    Each inner list will have 3 elements:
        a. island A
        b. island B
        c. cost of bridge connecting both islands
                       
    Each island is represented using a number
     
**Example:**                       
* `num_islands = 4`
* `bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]`
       
Input parameters explanation:
    1. Number of islands = 4
    2. Island 1 and 2 are connected via a bridge with cost = 1
       Island 2 and 3 are connected via a bridge with cost = 4
       Island 1 and 4 are connected via a bridge with cost = 3
       Island 4 and 3 are connected via a bridge with cost = 2
       Island 1 and 3 are connected via a bridge with cost = 10
       
In this example if we are connecting bridges like this...
* between 1 and 2 with cost = 1
* between 1 and 4 with cost = 3
* between 4 and 3 with cost = 2  

...then we connect all 4 islands with `cost = 6` which is the minimum traveling cost.


### Hint

In addition to using a graph, you may want to use a custom priority queue for solving this problem.

If you do not want to create a custom priority queue, you can use Python's `heapq` implementation.

Using the `heapq` module, you can convert an existing list of items into a heap. The following two functionalities can be very handy for this problem:

1. `heappush(heap, item)` — add `item` to the `heap`
2. `heappop(heap)` — remove the smallest item from the `heap`

Let's look at the above methods in action. We start by creating a list of integers.

### `heappush`


```python
# import moule
import heapq

# initialize an empty list 
heap = list()

# insert 5 into heap
heapq.heappush(heap, 6)

# insert 6 into heap
heapq.heappush(heap, 6)

# insert 2 into heap
heapq.heappush(heap, 2)

# insert 1 into heap
heapq.heappush(heap, 1)

# insert 9 into heap
heapq.heappush(heap, 9)

print("After pushing, heap looks like: {}".format(heap))
```

    After pushing, heap looks like: [1, 2, 6, 6, 9]


### `heappop`


```python
# pop and return smallest element from the heap
smallest = heapq.heappop(heap)   

print("Smallest element in the original list was: {}".format(smallest))

print("After popping, heap looks like: {}".format(heap))
```

    Smallest element in the original list was: 1
    After popping, heap looks like: [2, 6, 6, 9]


### `heappush` and `heappop` for items with multiple entries

Note: If you insert a tuple inside the heap, the element at 0th index of the tuple is used for comparision



```python
heap = list()

# the first element in the tuple is used to compare the tuple objects in the heap
heapq.heappush(heap, (0, 1))

heapq.heappush(heap, (-1, 5))

heapq.heappush(heap, (2, 0))

heapq.heappush(heap, (5, -1))

print("After pushing, now heap looks like: {}".format(heap))
```

    After pushing, now heap looks like: [(-1, 5), (0, 1), (2, 0), (5, -1)]



```python
# pop and return smallest element from the heap
smallest = heapq.heappop(heap)   

print("Smallest element in the original list was: {}".format(smallest))

print("After popping, heap looks like: {}".format(heap))
```

    Smallest element in the original list was: (-1, 5)
    After popping, heap looks like: [(0, 1), (5, -1), (2, 0)]


Now that you know about `heapq`, you can use it to solve the given problem. You are also free to create your own implementatin of Priority Queues.

Write code in the following function to find and return the minimum cost required to travel all islands via bridges.


```python
def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to returh minimum cost of connecting all islands
    """
    pass
```

<span class="graffiti-highlight graffiti-id_07rfocu-id_sgw589w"><i></i><button>Hide Solution</button></span>


```python
# Solution

# The following Solution makes use of one of Python's PriorityQueue implementation (heapq)
# For more details - https://thomas-cokelaer.info/tutorials/python/module_heapq.html
import heapq
def create_graph(num_islands, bridge_config):
    """
    Helper function to create graph using adjacency list implementation
    source: (neighbot, edge_cost)
    """
    adjacency_list = [list() for _ in range(num_islands + 1)]
    
    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]
        adjacency_list[source].append((destination, cost))
        adjacency_list[destination].append((source, cost))

    return adjacency_list

def minimum_cost(graph):
    """
    Helper function to find minimum cost of connecting all islands
    """
    
    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1
    
    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]
    
    
    # initialize starting list - (edge_cost, neighbor)
    heap = [(0, start_vertex)]
    total_cost = 0
    
    print ('visited: {}'.format(visited))
    print ('heap (cost,vertex): {}'.format(heap))
    print ('total cost: {}'.format(total_cost))
    
    iteration = 0

    while len(heap) > 0:
        print('--------iteration: {}'.format(iteration))
        
        # pop and return smallest element from heap (edge_cost, neighbor)
        cost, current_vertex = heapq.heappop(heap)
        
        print ('min (cost,vertex): ({},{})'.format(cost,current_vertex))
        print ('heap (cost,vertex): {}'.format(heap))
        
        # check if current_vertex is already visited (skip this iteration)
        if visited[current_vertex]:
            iteration += 1
            continue

        # else add cost to total-cost
        total_cost += cost
        
        print ('total cost: {}'.format(total_cost))
        
        print ('current vertex: {}'.format(current_vertex), end=" [")
        
        # loop through all the neighbors of the current vertex in the adjacent list of the graph
        for neighbor, edge_cost in graph[current_vertex]:
            print ('({},{})'.format(edge_cost, neighbor), end = " ")
            heapq.heappush(heap, (edge_cost, neighbor))
        print(']')
        print ('heap (cost,vertex): {}'.format(heap))
        
        # mark current vertex as visited
        visited[current_vertex] = True
        
        print ('visited: {}'.format(visited))
        iteration += 1

    return total_cost

def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)
```


```python
def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")
```


```python
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
```

    visited: [False, False, False, False, False, False]
    heap (cost,vertex): [(0, 1)]
    total cost: 0
    --------iteration: 0
    min (cost,vertex): (0,1)
    heap (cost,vertex): []
    total cost: 0
    current vertex: 1 [(1,2) (3,4) (10,3) ]
    heap (cost,vertex): [(1, 2), (3, 4), (10, 3)]
    visited: [False, True, False, False, False, False]
    --------iteration: 1
    min (cost,vertex): (1,2)
    heap (cost,vertex): [(3, 4), (10, 3)]
    total cost: 1
    current vertex: 2 [(1,1) (4,3) ]
    heap (cost,vertex): [(1, 1), (4, 3), (3, 4), (10, 3)]
    visited: [False, True, True, False, False, False]
    --------iteration: 2
    min (cost,vertex): (1,1)
    heap (cost,vertex): [(3, 4), (4, 3), (10, 3)]
    --------iteration: 3
    min (cost,vertex): (3,4)
    heap (cost,vertex): [(4, 3), (10, 3)]
    total cost: 4
    current vertex: 4 [(3,1) (2,3) ]
    heap (cost,vertex): [(2, 3), (3, 1), (4, 3), (10, 3)]
    visited: [False, True, True, False, True, False]
    --------iteration: 4
    min (cost,vertex): (2,3)
    heap (cost,vertex): [(3, 1), (10, 3), (4, 3)]
    total cost: 6
    current vertex: 3 [(4,2) (2,4) (10,1) ]
    heap (cost,vertex): [(2, 4), (3, 1), (4, 3), (10, 3), (4, 2), (10, 1)]
    visited: [False, True, True, True, True, False]
    --------iteration: 5
    min (cost,vertex): (2,4)
    heap (cost,vertex): [(3, 1), (4, 2), (4, 3), (10, 3), (10, 1)]
    --------iteration: 6
    min (cost,vertex): (3,1)
    heap (cost,vertex): [(4, 2), (10, 1), (4, 3), (10, 3)]
    --------iteration: 7
    min (cost,vertex): (4,2)
    heap (cost,vertex): [(4, 3), (10, 1), (10, 3)]
    --------iteration: 8
    min (cost,vertex): (4,3)
    heap (cost,vertex): [(10, 1), (10, 3)]
    --------iteration: 9
    min (cost,vertex): (10,1)
    heap (cost,vertex): [(10, 3)]
    --------iteration: 10
    min (cost,vertex): (10,3)
    heap (cost,vertex): []
    Pass



```python
num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
```

    visited: [False, False, False, False, False, False, False]
    heap (cost,vertex): [(0, 1)]
    total cost: 0
    --------iteration: 0
    min (cost,vertex): (0,1)
    heap (cost,vertex): []
    total cost: 0
    current vertex: 1 [(5,2) (8,3) ]
    heap (cost,vertex): [(5, 2), (8, 3)]
    visited: [False, True, False, False, False, False, False]
    --------iteration: 1
    min (cost,vertex): (5,2)
    heap (cost,vertex): [(8, 3)]
    total cost: 5
    current vertex: 2 [(5,1) (9,3) ]
    heap (cost,vertex): [(5, 1), (8, 3), (9, 3)]
    visited: [False, True, True, False, False, False, False]
    --------iteration: 2
    min (cost,vertex): (5,1)
    heap (cost,vertex): [(8, 3), (9, 3)]
    --------iteration: 3
    min (cost,vertex): (8,3)
    heap (cost,vertex): [(9, 3)]
    total cost: 13
    current vertex: 3 [(8,1) (9,2) ]
    heap (cost,vertex): [(8, 1), (9, 3), (9, 2)]
    visited: [False, True, True, True, False, False, False]
    --------iteration: 4
    min (cost,vertex): (8,1)
    heap (cost,vertex): [(9, 2), (9, 3)]
    --------iteration: 5
    min (cost,vertex): (9,2)
    heap (cost,vertex): [(9, 3)]
    --------iteration: 6
    min (cost,vertex): (9,3)
    heap (cost,vertex): []
    Pass



```python
num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
```

    visited: [False, False, False, False, False, False, False]
    heap (cost,vertex): [(0, 1)]
    total cost: 0
    --------iteration: 0
    min (cost,vertex): (0,1)
    heap (cost,vertex): []
    total cost: 0
    current vertex: 1 [(3,2) (9,5) ]
    heap (cost,vertex): [(3, 2), (9, 5)]
    visited: [False, True, False, False, False, False, False]
    --------iteration: 1
    min (cost,vertex): (3,2)
    heap (cost,vertex): [(9, 5)]
    total cost: 3
    current vertex: 2 [(3,1) (10,3) ]
    heap (cost,vertex): [(3, 1), (9, 5), (10, 3)]
    visited: [False, True, True, False, False, False, False]
    --------iteration: 2
    min (cost,vertex): (3,1)
    heap (cost,vertex): [(9, 5), (10, 3)]
    --------iteration: 3
    min (cost,vertex): (9,5)
    heap (cost,vertex): [(10, 3)]
    total cost: 12
    current vertex: 5 [(9,1) ]
    heap (cost,vertex): [(9, 1), (10, 3)]
    visited: [False, True, True, False, False, True, False]
    --------iteration: 4
    min (cost,vertex): (9,1)
    heap (cost,vertex): [(10, 3)]
    --------iteration: 5
    min (cost,vertex): (10,3)
    heap (cost,vertex): []
    total cost: 22
    current vertex: 3 [(10,2) (9,4) ]
    heap (cost,vertex): [(9, 4), (10, 2)]
    visited: [False, True, True, True, False, True, False]
    --------iteration: 6
    min (cost,vertex): (9,4)
    heap (cost,vertex): [(10, 2)]
    total cost: 31
    current vertex: 4 [(9,3) ]
    heap (cost,vertex): [(9, 3), (10, 2)]
    visited: [False, True, True, True, True, True, False]
    --------iteration: 7
    min (cost,vertex): (9,3)
    heap (cost,vertex): [(10, 2)]
    --------iteration: 8
    min (cost,vertex): (10,2)
    heap (cost,vertex): []
    Pass



```python

```
