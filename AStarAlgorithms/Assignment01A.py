import heapq

#TAKING THE INPUT
n,m=map(int, input().split())

start_r, start_c = map(int, input().split())
goal_r, goal_c = map(int, input().split())

maze = []
for _ in range(n):
    row_string = input().strip()
    row_array = []
    for char in row_string:
        if char == '#':
            row_array.append(1)
        else:
            row_array.append(0)
    maze.append(row_array)


class Node:
    def __init__(self,row,col,maze,g=0,h=0,f=0,path=""):
        self.row=row
        self.col=col
        self.maze=maze
        self.g=g
        self.h=h
        self.f=f
        self.path=path
    
    def __lt__(self, other):
        return self.f < other.f
    
def calculate_heuristic(current_node,goal_node):
    x_diff=abs(current_node.row - goal_node.row)
    y_diff=abs(current_node.col - goal_node.col)

    return x_diff+y_diff

def newNodeGenerator(openList,current_node,goal_node,new_dir,maze):
    if(new_dir=="U"):
        new_node=Node(current_node.row-1,current_node.col,maze)
    elif(new_dir=="D"):
        new_node=Node(current_node.row+1,current_node.col,maze)
    elif(new_dir=="L"):
        new_node=Node(current_node.row,current_node.col-1,maze)
    elif(new_dir=="R"):
        new_node=Node(current_node.row,current_node.col+1,maze)
    
    new_node.path=current_node.path+new_dir
    new_node.g=current_node.g+1
    new_node.h=calculate_heuristic(new_node,goal_node)
    new_node.f=new_node.g + new_node.h

    heapq.heappush(openList,new_node)

def aStarSearch():

    start_node=Node(start_r,start_c,maze)
    goal_node=Node(goal_r,goal_c,maze)
    start_node.h=calculate_heuristic(start_node,goal_node)
    start_node.f=start_node.h

    openList=[]
    visited=set()

    heapq.heappush(openList,start_node)

    while(len(openList)!=0):
        current_node=heapq.heappop(openList)
        if (current_node.row==goal_node.row and current_node.col==goal_node.col):
            return current_node.path,current_node.g

        coordinates = (current_node.row, current_node.col)
        if coordinates in visited:
            continue
        visited.add(coordinates)


        if(current_node.row > 0 and current_node.maze[current_node.row-1][current_node.col]==0):
            newNodeGenerator(openList,current_node,goal_node,"U",maze)
        
        if(current_node.row < len(maze)-1 and current_node.maze[current_node.row+1][current_node.col]==0):
            newNodeGenerator(openList,current_node,goal_node,"D",maze)

        if(current_node.col > 0 and current_node.maze[current_node.row][current_node.col-1]==0):
            newNodeGenerator(openList,current_node,goal_node,"L",maze)

        if(current_node.col < len(maze[0])-1 and current_node.maze[current_node.row][current_node.col+1]==0):
            newNodeGenerator(openList,current_node,goal_node,"R",maze)

    return "Path not Found",-1
        
path,cost=aStarSearch()
print(cost)
print(path)



