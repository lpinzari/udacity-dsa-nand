
# Dijkstra's Algorithm
In this exercise, you'll implement Dijkstra's algorithm. First, let's build the graph.
## Graph Representation
In order to run Dijkstra's Algorithm, we'll need to add distance to each edge. We'll use the `GraphEdge` class below to represent each edge between a node.


```python
class GraphEdge(object):
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance
```

The new graph representation should look like this:


```python
class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)

class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            #node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)
```

Now let's create the graph.


```python
node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
graph.add_edge(node_u, node_a, 4) # u -> a
graph.add_edge(node_u, node_c, 6) # u -> c
graph.add_edge(node_u, node_d, 3) # u -> d
graph.add_edge(node_d, node_u, 3) # d -> u
graph.add_edge(node_d, node_c, 4) # d -> c
graph.add_edge(node_a, node_u, 4) # a -> u
graph.add_edge(node_a, node_i, 7) # a -> i
graph.add_edge(node_c, node_d, 4) # c -> d
graph.add_edge(node_c, node_u, 6) # c -> u
graph.add_edge(node_c, node_i, 4) # c -> i
graph.add_edge(node_c, node_t, 5) # c -> t
graph.add_edge(node_i, node_a, 7) # i -> a
graph.add_edge(node_i, node_c, 4) # i -> c
graph.add_edge(node_i, node_y, 4) # i -> y
graph.add_edge(node_t, node_c, 5) # t -> c
graph.add_edge(node_t, node_y, 5) # t -> y
graph.add_edge(node_y, node_i, 4) # y -> i
graph.add_edge(node_y, node_t, 5) # y -> t

# To verify that the graph is created accurately.
# Let's just print all the parent nodes and child nodes.
for each in graph.nodes:
    print('parent node = ',each.value,end='\nchildren (node,distance)\n')
    for edge in each.edges:
        print('({},{})'.format(edge.node.value,edge.distance),end=' ')
    print('\n')
```

    parent node =  U
    children (node,distance)
    (A,4) (C,6) (D,3) 
    
    parent node =  D
    children (node,distance)
    (U,3) (C,4) 
    
    parent node =  A
    children (node,distance)
    (U,4) (I,7) 
    
    parent node =  C
    children (node,distance)
    (D,4) (U,6) (I,4) (T,5) 
    
    parent node =  I
    children (node,distance)
    (A,7) (C,4) (Y,4) 
    
    parent node =  T
    children (node,distance)
    (C,5) (Y,5) 
    
    parent node =  Y
    children (node,distance)
    (I,4) (T,5) 
    


## Implementation
Using what you've learned, implement Dijkstra's Algorithm to find the shortest distance from the "U" node to the "Y" node. 


```python
import math

def dijkstra(start_node, end_node):
    pass


print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(node_u, node_y)))
```

<span class="graffiti-highlight graffiti-id_6vmf0hp-id_cjtybve"><i></i><button>Hide Solution</button></span>


```python
import math

def print_dict(d):
    
    for key,value in d.items():
        print ('{} : {}'.format(key.value,value), end="    ")
    print("\n")

def dijkstra(start_node, end_node):
    # initialize single source distances
    distance_dict = {node: math.inf for node in graph.nodes}
    shortest_path_to_node = {}
    
    # the starting node has distance zero start_node -> start_node distance: 0
    distance_dict[start_node] = 0
    
    while distance_dict:
        # Pop the shorest path
        # sort the items of the distance_dict, i.e x = (node, distance), based on the value key (x[1]: distance)
        # as applied to each element (x) of the list and retrieve the first element of the sorted list
        # current_node is the node with the shortest path from the start_node
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]
        print_dict(distance_dict)
        # update the shortest path distance to the current node and remove the node from the dictionary
        shortest_path_to_node[current_node] = distance_dict.pop(current_node)
        print_dict(shortest_path_to_node)
        
        print(current_node.value, end=': ')
        for edge in current_node.edges:
            print('({},{})'.format(edge.node.value,edge.distance),end=' ')
        print('\n')
        
        for edge in current_node.edges:
            # if the node has not been visited then compute and update distance
            if edge.node in distance_dict:
                new_node_distance = node_distance + edge.distance
                if distance_dict[edge.node] > new_node_distance:
                    distance_dict[edge.node] = new_node_distance
        print("----------------------------")
    
    return shortest_path_to_node[end_node]

print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(node_u, node_y)))
```

    U : 0    D : inf    A : inf    C : inf    I : inf    T : inf    Y : inf    
    
    U : 0    
    
    U: (A,4) (C,6) (D,3) 
    
    ----------------------------
    D : 3    A : 4    C : 6    I : inf    T : inf    Y : inf    
    
    U : 0    D : 3    
    
    D: (U,3) (C,4) 
    
    ----------------------------
    A : 4    C : 6    I : inf    T : inf    Y : inf    
    
    U : 0    D : 3    A : 4    
    
    A: (U,4) (I,7) 
    
    ----------------------------
    C : 6    I : 11    T : inf    Y : inf    
    
    U : 0    D : 3    A : 4    C : 6    
    
    C: (D,4) (U,6) (I,4) (T,5) 
    
    ----------------------------
    I : 10    T : 11    Y : inf    
    
    U : 0    D : 3    A : 4    C : 6    I : 10    
    
    I: (A,7) (C,4) (Y,4) 
    
    ----------------------------
    T : 11    Y : 14    
    
    U : 0    D : 3    A : 4    C : 6    I : 10    T : 11    
    
    T: (C,5) (Y,5) 
    
    ----------------------------
    Y : 14    
    
    U : 0    D : 3    A : 4    C : 6    I : 10    T : 11    Y : 14    
    
    Y: (I,4) (T,5) 
    
    ----------------------------
    Shortest Distance from U to Y is 14



```python

```
