import heapq

vertices , edges = map(int, input())
start_state , goal_sstate = map(int, input())

nodes = {}

for i in range (vertices):
    node,heuristic = map(int, input())
    nodes[node]=heuristic

connections={}

for i in range (edges):
    node1, node2 = map(int, input())
    connections[node1]=node2


    
