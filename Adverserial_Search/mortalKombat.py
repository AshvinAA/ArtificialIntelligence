import random,math 

first_turn = int(input())

leaf_nodes = [random.choice([1,-1]) for _ in range(32)]

def alpha_beta(depth , nodes_index , is_maxing , alpha ,beta , leaf_nodes):
    if depth==5:
        return leaf_nodes[nodes_index]
    
    if is_maxing:
        best_score = -math.inf

        for i in range(2):
            child_index = nodes_index*2+i

            score = alpha_beta(depth+1 , child_index , False,alpha , beta ,leaf_nodes)

            best_score = max(best_score,score)
            alpha= max(alpha ,best_score)

            if(alpha >= beta):
                break
        
        return best_score
    else:
        best_score = math.inf

        for i in range(2):
            child_index = nodes_index*2+i

            score = alpha_beta(depth+1 , child_index , True,alpha , beta , leaf_nodes)

            best_score = min(best_score,score)
            beta = min(beta, best_score)

            if(beta <= alpha):
                break
        return best_score


winner=0 
if(first_turn)==1:
    winner = alpha_beta(0,0,True,math.inf , -math.inf , leaf_nodes) 
else:
    winner = alpha_beta(0,0,False,math.inf , -math.inf , leaf_nodes)  

if(winner == -1):
    print("Scorpion Wins")
else:
    print("Sub Zero Wins")