
# Graph Breadth First Search
In this exercise, you'll see how to do a breadth first search on a graph. To start, let's create a graph class in Python.


```python
class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list
        
    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)
```

Now let's create the graph.


```python
nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

print('G: {} -> {} -> {}'.format(nodeG.children[0].value,nodeG.children[1].value,nodeG.children[2].value))
print('R: {} -> {} -> {} -> {}'.format(nodeR.children[0].value,nodeR.children[1].value,nodeR.children[2].value,nodeR.children[3].value))
print('A: {} -> {}'.format(nodeA.children[0].value,nodeA.children[1].value))
print('P: {} -> {}'.format(nodeP.children[0].value,nodeP.children[1].value))
print('H: {} -> {}'.format(nodeH.children[0].value,nodeH.children[1].value))
print('S: {}'.format(nodeS.children[0].value))

# To verify that the graph is created accurately.
# Let's just print all the parent nodes and child nodes.
for each in graph1.nodes:
    print('parent node = ',each.value,end='\nchildren\n')
    for each in each.children:
        print(each.value,end=' ')
    print('\n')
```

    G: R -> A -> H
    R: G -> A -> P -> S
    A: R -> G
    P: R -> H
    H: G -> P
    S: R
    parent node =  S
    children
    R 
    
    parent node =  H
    children
    G P 
    
    parent node =  G
    children
    R A H 
    
    parent node =  P
    children
    R H 
    
    parent node =  R
    children
    G A P S 
    
    parent node =  A
    children
    R G 
    


## Implement BFS
Using what you know about BFS for trees and DFS for graphs, let's do BFS for graphs. Implement the `bfs_search` to return the `GraphNode` with the value `search_value` starting at the `root_node`.


```python
def bfs_search(root_node, search_value):
    pass
```

<span class="graffiti-highlight graffiti-id_fg1wpq1-id_g7fi7m5"><i></i><button>Hide Solution</button></span>


```python
def bfs_search(root_node, search_value):
    visited = []
    queue = [root_node]
    
    visited.append(root_node)
    print('bfs_search({}, {})'.format(root_node.value,search_value))
    print('Queue: [{}]'.format(queue[0].value))
    print('Visited: [{}]'.format(visited[0].value))
    
    iteration = 0
    
    while len(queue) > 0 and iteration <= 15:
        # FIFO: we remove the first element we inserted in the list
        current_node = queue.pop(0)
        
        
        print('\t ---- iteration: {}'.format(iteration))
        
        print('Queue: [', end ="")
        for i in range(0,len(queue)):
            if i < len(queue) - 1:
                print(queue[i].value, end = ", ")
            else:
                print(queue[i].value, end = "")
        print(']')
        
        
        print('current_node: {}'.format(current_node.value))

        if current_node.value == search_value:
            return current_node

        for child in current_node.children:
            if child not in visited:
                queue.append(child)
                visited.append(child)
                
        print('Queue: [', end ="")
        for i in range(0,len(queue)):
            if i < len(queue) - 1:
                print(queue[i].value, end = ", ")
            else:
                print(queue[i].value, end = "")
        print(']')
                
        iteration += 1
        
        print('Visited: [', end ="")
        for i in range(0,len(visited)):
            if i < len(visited) - 1:
                print(visited[i].value, end = ", ")
            else:
                print(visited[i].value, end = "")
        print(']')
    
    return None
```

### Tests


```python
assert nodeA == bfs_search(nodeS, 'A')
print('-----------------------------')
assert nodeS == bfs_search(nodeP, 'S')
print('-----------------------------')
# assert nodeR == bfs_search(nodeH, 'R')
# print('-----------------------------')
assert None == bfs_search(nodeH, 'W')
```

    bfs_search(S, A)
    Queue: [S]
    Visited: [S]
    	 ---- iteration: 0
    Queue: []
    current_node: S
    Queue: [R]
    Visited: [S, R]
    	 ---- iteration: 1
    Queue: []
    current_node: R
    Queue: [G, A, P]
    Visited: [S, R, G, A, P]
    	 ---- iteration: 2
    Queue: [A, P]
    current_node: G
    Queue: [A, P, H]
    Visited: [S, R, G, A, P, H]
    	 ---- iteration: 3
    Queue: [P, H]
    current_node: A
    -----------------------------
    bfs_search(P, S)
    Queue: [P]
    Visited: [P]
    	 ---- iteration: 0
    Queue: []
    current_node: P
    Queue: [R, H]
    Visited: [P, R, H]
    	 ---- iteration: 1
    Queue: [H]
    current_node: R
    Queue: [H, G, A, S]
    Visited: [P, R, H, G, A, S]
    	 ---- iteration: 2
    Queue: [G, A, S]
    current_node: H
    Queue: [G, A, S]
    Visited: [P, R, H, G, A, S]
    	 ---- iteration: 3
    Queue: [A, S]
    current_node: G
    Queue: [A, S]
    Visited: [P, R, H, G, A, S]
    	 ---- iteration: 4
    Queue: [S]
    current_node: A
    Queue: [S]
    Visited: [P, R, H, G, A, S]
    	 ---- iteration: 5
    Queue: []
    current_node: S
    -----------------------------
    bfs_search(H, W)
    Queue: [H]
    Visited: [H]
    	 ---- iteration: 0
    Queue: []
    current_node: H
    Queue: [G, P]
    Visited: [H, G, P]
    	 ---- iteration: 1
    Queue: [P]
    current_node: G
    Queue: [P, R, A]
    Visited: [H, G, P, R, A]
    	 ---- iteration: 2
    Queue: [R, A]
    current_node: P
    Queue: [R, A]
    Visited: [H, G, P, R, A]
    	 ---- iteration: 3
    Queue: [A]
    current_node: R
    Queue: [A, S]
    Visited: [H, G, P, R, A, S]
    	 ---- iteration: 4
    Queue: [S]
    current_node: A
    Queue: [S]
    Visited: [H, G, P, R, A, S]
    	 ---- iteration: 5
    Queue: []
    current_node: S
    Queue: []
    Visited: [H, G, P, R, A, S]



```python

```
