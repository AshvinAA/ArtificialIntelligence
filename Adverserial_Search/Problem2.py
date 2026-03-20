import math 

#set of remaining alphabets
remaining={"A","B","C","D"}
id=[1,0,0,8]
state=[]

def utility(state):
    i=0
    val=0
    for char in state:
        val+=ord(char)
        i+=1
    return val

def minimax(state,remaining,maxing,alpha,beta):
    if(len(remaining)==0):
        return state,utility(state)
    if(maxing==True):
        best_score = -math.inf

        for character in list(remaining):
            state.append(character)
            remaining.remove(character)
            new_state,score= minimax(state, remaining , False ,alpha , beta)
            
            remaining.add(character)
            best_score= max(best_score , score)
            if(score >= beta ): return state,score 
            if(score > alpha ): alpha = score
        
        return state,best_score

    else:
        best_score = math.inf

        for character in remaining:
            state.append(character)
            remaining.remove(character)
            new_state,score= minimax(state, remaining  , True ,alpha , beta)
            state.pop()
            remaining.add(character)
            best_score= min(best_score , score)
            if(score <= alpha ): return state,score 
            if(score < beta ): beta = score

        return state,best_score

new_state,new_score= minimax(state , remaining, True , math.inf , -math.inf)

print(new_state)
print(new_score)