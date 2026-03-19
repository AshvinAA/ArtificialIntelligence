from queue import Queue

state=[" "]*9

state=["X","O","X","O","X","O","O","X","O"]



def returnRow(state,rowNumber):
    arr=[]
    for i in range(3):
        index=i+3*rowNumber
        arr.append(state[index])
    return arr

def returnColumn(state,colNumber):
    arr=[]
    index=0
    for i in range(3):
        arr.append(state[index+colNumber])
        index+=3
    return arr

def returnDiagonal(state,diaNumber):
    if(diaNumber==0):
        return [state[0],state[4],state[8]]
    else:
        return [state[2],state[4],state[6]]

def isSame(arr):
    return arr[0] == arr[1] == arr[2]
        
def winner(grid):
    for i in range(3):
        row=returnRow(state,i)
        if(isSame(row)):
            return row[0]
    for i in range(3):
        column=returnColumn(state,i)
        if(isSame(column)):
            return column[0]
    
    for i in range(2):
        diagonal = returnDiagonal(state,i)
        if(isSame(diagonal)):
            return diagonal[0]
    return "N"
    

def utility(grid):
    
    win = winner(grid)
    
    if(win)=="X":
        return -100
    elif(win)=="O":
        return 100
    else:
        return 0
    

        

print(winner(state))

