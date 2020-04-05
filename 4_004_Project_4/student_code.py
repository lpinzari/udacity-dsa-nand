from heapq import heappush, heappop # needed for Priority Queue
import math # needed for computing the distance

#----------------- Auxiliary data structure -------------#

# The Python standard library provides a Heap data structure, but not a Priory Queue
# so we need to implement one ourselves.

class PriorityQueue:
    
    def __init__(self, iterable = []):
        self.heap = []
        for value in iterable:
            heappush(self.heap,(0,value))
            
    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))
        
    def pop(self):
        priority, value = heappop(self.heap)
        return value
    
    def __len__(self):
        return len(self.heap)
    
#-------------------- Helper functions ------------------------#

def reconstruct_path(came_from, start, end):
    """
    Given the set of predecessors for each node on the map, an origin (start) and a destination (end)
    returns a path as we need to show from start to end.
    Args:
     (dict) came_from: (int) keys: node ID. (int) values: node's predecessor
     (int) start: ID of the origin intersection
     (int) goal: ID of the destination intersection
    Returns:
     (float): Euclidean distance
    Example:
    >>> come_from = {2: 1, 3: 1, 4: 3, 5: 4, 6: 4}
    >>> reconstruct_path(come_from, 1, 5)
    ['1', '3', '4', '5']
    """
    reversed_path = [end]
    
    while end != start:
        end = came_from[end]
        reversed_path.append(end)
        
    return list(reversed(reversed_path))

def distance(xy_1, xy_2):
    
    """
    Given the cartesian coordinates (x,y) of two points,
    returns the Euclidean distance aka crow fly distance
    
    Args:
     (list) xy_1: [float, float] first point
     (list) xy_2: [float, float] second point
    Returns:
     (float): Euclidean distance
    """
    
    x1 = xy_1[0]
    y1 = xy_1[1]
    
    x2 = xy_2[0]
    y2 = xy_2[1]
    
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def shortest_path(M: object, start: int, goal: int) -> list:
    
    """
    Given a map, an origin (start) and a destination (goal),
    returns the shortest path based on A* algorithm.
    Code adapted from: https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/a-search-in-python
    
    Args:
     (object) map: map of the 2D space
     (int) start: ID of the origin intersection
     (int) goal: ID of the destination intersection
     
    Returns:
     (list): list of integers representing a path from start to destination
     
    Note:
     The ID is a natural number in the interval [0 ... N-1], where N is the number of intersections (nodes) on the map 
    """
    
    # dictionary of Map intersections coordinates (x,y)
    nodes_xy = M.intersections
    
    # destination coordinates
    goal_xy = nodes_xy[goal]
    
    # list of lists of adjacent nodes
    nodes_connections = M.roads
    
    # Set of integers to track the visited nodes in the search
    visited = set()
    
    # Dictionary to track the predecessors in the path
    come_from = dict()
    
    # initialize single nodes distance from the origin
    nodes_id = nodes_xy.keys()        
    dist_from_start = {node_id: math.inf for node_id in nodes_id}
    dist_from_start[start] = 0
    
    # create frontier to be expanded as a PriorityQueue and add the origin to the PriorityQueue
    frontier = PriorityQueue()
    frontier.add(start)
    
    # loop until all the nodes in the frontier have been explored
    while frontier:
        
        # retrieve the node with the minimum cost from frontier
        node = frontier.pop()
        
        # check if the node has been processed
        if node in visited:
            continue
            
        # goal node found: Terminate search
        if node == goal:
            return reconstruct_path(come_from, start, node)
        
        # mark the current node as visited
        visited.add(node)
        
        # examine all possible neighbors and update the cost function f
        # for nodes near the current node
        
        node_xy = nodes_xy[node] # current node's coordinates
        
        for neighbor in nodes_connections[node]:
            
            neighbor_xy = nodes_xy[neighbor] # neighbor's coordinates
            
            # total distance travelled to reach the neighbor
            cost_g = dist_from_start[node] + distance(node_xy, neighbor_xy)
            
            # estimated distance for the remaining distance to goal
            cost_h = distance(neighbor_xy, goal_xy)
            
            # estimated cost of the path from start to goal via neighbor's position 
            cost_f = cost_g + cost_h
            
            # check if the actual distance travelled is better of the distance calculated previously.
            if cost_g < dist_from_start[neighbor]:
                
                # update neighbor's distance, precedessor. And add it to the Priority Queue
                dist_from_start[neighbor] = cost_g
                come_from[neighbor] = node
                frontier.add(neighbor, priority = cost_f)
                
    # there is no solution, the graph may be not fully connected
    return None