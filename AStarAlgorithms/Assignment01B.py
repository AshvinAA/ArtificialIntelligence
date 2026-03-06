from queue import Queue

class Node:
    def __init__(self,val,h):
        self.val=val
        self.h=h
        self.edge=[]
    
nodes = {}

vertices , edges = map(int, input().split())
start_state , goal_state = map(int, input().split())


for i in range (vertices):
    node,heuristic = map(int, input().split())
    nodes[node]=Node(node,heuristic)

for i in range (edges):
    node1, node2 = map(int, input().split())
    current_node = nodes[node1]
    current_node.edge.append(nodes[node2])
    nodes[node2].edge.append(nodes[node1])


def find_cost(start_node, goal_node):

    queue = Queue()

    queue.put(start_node)

    visited=[]

    cost=-1
    while(len(queue)>0):
        current_node=queue.get()
        cost+=1
        visited.append(current_node)

        if(current_node == goal_node):
            return cost

        for neighbours in current_node.edges:
            if neighbours not in visited:
                queue.put(neighbours)
    

goal_node=Node(goal_state,0)

costs={}

for node in nodes:
    cost= find_cost(node,goal_node)
    costs[node] = cost

def admissibility_checker():
    for node in nodes:
        if (costs[node] > node.h):
            print(0)
            return
    print(1)

admissibility_checker()


    
