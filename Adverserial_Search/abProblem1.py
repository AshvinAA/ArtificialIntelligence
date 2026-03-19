from queue import Queue
import math

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

def isSame(state):
    return state[0] == state[1]  and state[1] == state[2]

def isTerminal(state):
    for i in range(len(state)):
        if(state[i] == " "):
            return False
    return True
        
def utility(state):
    for i in range(3):
        row=returnRow(state,i)
        if(isSame(row)):
            if(row[0] == "X"):
                return -100
            else:
                return 100
    for i in range(3):
        column=returnColumn(state,i)
        if(isSame(column)):
            if(column[0] == "X"):
                return -100
            else:
                return 100
        
    for i in range(2):
        diagonal = returnDiagonal(state,i)
        if(isSame(diagonal)):
            if(diagonal[0] == "X"):
                return -100
            else:
                return 100
    return 0

def heuristic_comparator(line):
    numO=0
    numX=0
    empty=0

    for i in range(3):
        if(line[i] == "O"):
            numO+=1
        elif(line[i]=="X"):
            numX+=1
        else:
            empty+=1
    if(empty==3):
        return 0
    
    if(numO >=1):
        if(numX>0):
            return 0
        else:
            if(numO==2):
                return 10
        return 1
    else:
        if(numX == 2):
            return -10
        return 1


def heuristic(state):
    total_score=0
    for i in range(3):
        row=returnRow(state,i)

        heuristic_value = heuristic_comparator(row)
        total_score+=heuristic_value
        
    for i in range(3):
        column=returnColumn(state,i)

        heuristic_value = heuristic_comparator(column)
        total_score+=heuristic_value
        
    
    for i in range(2):
        diagonal = returnDiagonal(state,i)

        heuristic_value = heuristic_comparator(diagonal)
        total_score+=heuristic_value

    return total_score
        

def minimax(state , depth , is_agent_turn):

    if(isTerminal(state)):
        return utility(state)

    if(depth == 0):
        return heuristic(state)
    
    if( is_agent_turn == True ):
        best_score = -math.inf

        for i in range(len(state)):
            if(state[i]==" "):
                state[i]="O"
                score = minimax(state , depth -1 , False)
                state[i]=" "
                best_score=max(score , best_score)
        return best_score
    else:
        best_score= math.inf

        for i in range(len(state)):
            if(state[i]==" "):
                state[i]="X"
                score = minimax(state , depth -1 , True)
                state[i]=" "
                best_score=min(score , best_score)
        return best_score