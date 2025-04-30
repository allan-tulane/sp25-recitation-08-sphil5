from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    heap = []
    heappush(heap, (0, 0, source))

    shortest_paths = {vertex: (float('inf'), float('inf')) for vertex in graph} # initialize a dictionary to store the shortest paths 
    shortest_paths[source] = (0, 0) # set the shortest path to the source node as 0

    while heap:
      current_weight, current_vertex = heappop(heap) # pop the vertex with the smallest weight
      if current_weight > shortest_paths[current_vertex][0]:
        continue # skip the vertex if the current weight is greater than the shortest path weight
      for neighbor in graph[current_vertex]:
        new_weight = current_weight + 1 # update the weight of the neighbor 
        new_edges = shortest_paths[current_vertex][1] + 1 #update the edges 

        if new_weight < shortest_paths[neighbor][0] or (new_weight == shortest_paths[neighbor][0] and new_edges < shortest_paths[neighbor][1]): 
          shortest_paths[neighbor] = (new_weight, new_edges) # update the shortest path wight and edges 
          heappush(heap, (new_weight, neighbor)) # push the neighbor to the heap 

    return shortest_paths 
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    parents = {vertex: None for vertex in graph} # initialize parents dictionary 
    queue = deque([source]) # initialize queue 
    visited = set([source]) # keep track of visited nodes 
  
    while queue: 
        vertex = queue.popleft() # dequeue the vertex
        for neighbor in graph[vertex]: # iterate through the neighbors
            if neighbor not in visited: 
                parents[neighbor] = vertex # if the neighbor has not been visited, set its parent to the current vertex 
                queue.append(neighbor) # append the neighbor to the queue 

    return parents 

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
    while destination in parents:
        path.append(destination) # add the current node to the path
        destination = parents[destination] # move to the parent node 
        
      
    path.reverse() # reverse the path for the correct order 
    return path[:-1] # return the path and exclude the destination node 

