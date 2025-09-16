# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:42:47 2022

@author: Fatim
"""

# This will create the "tree" with the nodes

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F', 'G'],
  'D' : ['H'],
  'E' : [],
  'F' : ['H'],
  'G' : [],
  'H' : []
}


visited = [] # A list called visited is used to track visited nodes.


queue = [] # Each node that has to be visited is managed by the queue.



def bfs(visited, graph, node): # Creates a function, then pass parameters through it.
 
                            
 # Then it includes the starting node in the visited and waiting lists.

 visited.append(node)
 queue.append(node)
 
 
 while queue:            # while statemet to remove it from the queue
     a = queue.pop(0)
     print (a, end = " ")
     for neighbour in graph[a]:         # A for statement that will go to the node's unvisited neighbour and add it to the visited list and the queue
         if neighbour not in visited:
             visited.append(neighbour)
             queue.append(neighbour)
             
             
             
print ("The following is the Breadth-First search: ")

# Driver code
bfs(visited, graph, 'A')