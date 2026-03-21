import math 

#set of remaining alphabets
remaining={"A","B","C","D"}
id=[1,0,0,8]
state=[]

#id[0] * char[0] + id[1]*char[1] .... 
def utility(state):
    i=0
    val=0
    for char in state:
        val+=id[i] * ord(char)
        i+=1
    return val


def minimax(state,remaining,maxing,alpha,beta):
    if(len(remaining)==0):
        return list(state),utility(state)
    if(maxing==True):
        best_score = -math.inf
        best_state=[]

        for character in sorted(list(remaining)):
            state.append(character)
            remaining.remove(character)
            new_state,score= minimax(state, remaining , False ,alpha , beta)
            state.pop()
            
            if(score>best_score):
                best_score=score
                best_state=list(new_state)
            remaining.add(character)
            best_score = max(best_score , score)
            if(score >= beta ): return new_state,score 
            if(score > alpha ): alpha = score
        
        return best_state,best_score

    else:
        best_score = math.inf
        best_state=[]

        for character in sorted(list(remaining)):
            state.append(character)
            remaining.remove(character)
            new_state,score= minimax(state, remaining  , True ,alpha , beta)
            state.pop()

            if(score<best_score):
                best_score=score
                best_state=list(new_state)
            
            remaining.add(character)
            best_score= min(best_score , score)
            if(score <= alpha ): return new_state,score 
            if(score < beta ): beta = score

        return best_state,best_score

new_state,new_score= minimax(state , remaining, True , -math.inf , math.inf)

print(new_state)
print(new_score)