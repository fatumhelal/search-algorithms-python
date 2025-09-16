# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:00:33 2022

@author: Fatim
"""

# This will create the "tree" with the nodes

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []

}


visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs to check if the current node is unvisited 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("The following is the Depth-First Search: ")

# Driver Code
dfs(visited, graph, 'A')      # A is the starting node 







