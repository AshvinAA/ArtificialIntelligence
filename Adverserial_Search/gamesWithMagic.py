import random,math 

first_turn = int(input())

leaf_nodes = [3,6,2,3,7,1,2,0]

def alpha_beta(depth , nodes_index , is_maxing , alpha ,beta , leaf_nodes , dark_magic ,dark_flag):
    if depth==3:
        return leaf_nodes[nodes_index]
    
    if is_maxing:
        best_score = -math.inf

        for i in range(2):
            child_index = nodes_index*2+i

            score = alpha_beta(depth+1 , child_index , False,alpha , beta ,leaf_nodes ,dark_magic ,dark_flag)

            best_score = max(best_score,score)
            alpha= max(alpha ,best_score)

            if(alpha >= beta):
                break
        
        return best_score
    else:
        best_score = math.inf

        for i in range(2):
            child_index = nodes_index*2+i

            score = alpha_beta(depth+1 , child_index , True,alpha , beta , leaf_nodes , dark_magic , dark_flag )     
            if dark_flag:
                best_score = max(best_score,score) - dark_magic
            else:
                best_score = min(best_score,score)

            beta = min(beta, best_score)

            if(beta <= alpha):
                break

        return best_score


print( alpha_beta(0,0,True,math.inf,-math.inf , leaf_nodes , 2 , True) )