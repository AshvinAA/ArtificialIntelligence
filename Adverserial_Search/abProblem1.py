from queue import Queue

grid=[][]

def winner(grid):
    for i in range(len(grid)):
        if(grid[i][0] == grid[i][1] == grid[i][2]):
            return grid[i][0]
    for i in range(len(grid)):
        if(grid[0][i] == grid[1][i] == grid[2][i]):
            return grid[0][i]
    
    if(grid[0][2] == grid[1][1] == grid[2][0]):
        return grid[0][2]
    if(grid[0][0] == grid[1][1] == grid[2][2]):
        return grid[0][0]
    return "N"

def utility(grid):
    
    win = winner(grid)
    
    if(win)=="X":
        return -100
    elif(win)=="O":
        return 100
    else:
        return 0
    
            
        



