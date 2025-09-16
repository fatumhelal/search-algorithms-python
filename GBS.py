# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:20:13 2022

@author: Fatim
"""


# This will create the "tree" with the nodes & their heuristics 

graph = {
'A':[('B',9), ('C',6)],
'B':[('D',11), ('E',4)],
'C':[('F',8), ('G',14)],
'D':[],
'E':[('H',0)],
'F':[('H',0)],
'G':[('H',0)]
}



def gbs(start, target, graph, queue=[], visited=[]):      # def gbs function which takes parameters and creates two lists
 if start not in visited:
     print(start)
     visited.append(start)
     
     
 queue=queue+[x for x in graph[start] if x[0][0] not in visited]      #This will check which node is the shortest path
 queue.sort(key=lambda x:x[1])
 
 
 if queue[0][0]==target:         # This checks if the goal node has been located
     print(queue[0][0])
 else:
     processing=queue[0]
     queue.remove(processing)
     gbs(processing[0], target, graph, queue, visited)
     

print("The following is the Greedy best-first Search: ")
 
# Driver code    
gbs('A', 'H', graph)   # A is the starting node and H is the goal node

