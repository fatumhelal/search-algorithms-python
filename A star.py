# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:44:18 2022

@author: Fatim
"""

# This will create the "tree" with equal values for all nodes

graph=[
       ['A','B',1,3], 
       ['A','C',2,4], 
       ['A','H',7,0], 
       ['B','D',4,2], 
       ['B','E',6,6],
       ['C','F',3,3],
       ['C','G',2,1],
       ['D','E',7,6],
       ['D','H',5,0],
       ['F','H',1,0],
       ['G','H',2, 0]
 ]

 # initailizing temp & temp1 as a list
temp = []
temp1 = []
for i in graph:         
    temp.append(i[0])
    temp1.append(i[1])
nodes = set(temp).union(set(temp1))    # set the nodes


def astar(graph, costs, open, closed, cur_node):  # a def astar function that will 
                                                # see which path has least cost to reach the goal node
    if cur_node in open:
        # remove cur_node from the open list and then...
            open.remove(cur_node)
    # add it to the closed list 
    closed.add(cur_node)
    for i in graph:
        if(i[0] == cur_node and costs[i[0]]+i[2]+i[3] < costs[i[1]]):
            open.add(i[1])
            costs[i[1]] = costs[i[0]]+i[2]+i[3]
            path[i[1]] = path[i[0]] + ' , ' + i[1]   # when printing out the path it 
                                                     #  will add a , after each node e.g. a, b, c

    costs[cur_node] = 999999
    small = min(costs, key=costs.get)
    if small not in closed:
         astar(graph, costs, open,closed, small)
costs = dict()
temp_cost = dict()
path = dict()
for i in nodes:
 costs[i] = 999999
 path[i] = ' '

# In this open it's a list of nodes which have been visited
open = set()  

# And closed is a list of nodes which have been visited 
closed = set()


print("The folllowing is the A star algorithm: ")

# This will allow the user to enter the start node
start_node = input("Enter the start node: ")
open.add(start_node)
path[start_node] = start_node
costs[start_node] = 0
astar(graph, costs, open, closed, start_node)

# This will allow the user to enter the goal node
goal_node = input("Enter the target node: ")

# This will print out the path with the least cost 
print("The path with the least cost is: ",path[goal_node])
