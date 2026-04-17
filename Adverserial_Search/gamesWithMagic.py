import random,math 

leaf_nodes = [3,6,2,3,7,1,2,0]

def alpha_beta(depth , nodes_index , is_maxing , alpha ,beta , leaf_nodes ):
    if depth==3:
        return leaf_nodes[nodes_index]

    if is_maxing:
        best_score = -math.inf

        for i in range(2):
            child_index = nodes_index*2+i

            score = alpha_beta(depth+1 , child_index , False,alpha , beta ,leaf_nodes )

            best_score = max(best_score,score)
            alpha= max(alpha ,best_score)

            if(alpha >= beta):
                break
        
        return best_score
    else:
        best_score = math.inf

        for i in range(2):
            child_index = nodes_index*2+i

            score = alpha_beta(depth+1 , child_index , True,alpha , beta , leaf_nodes )     

            best_score = min(best_score,score)

            beta = min(beta, best_score)

            if(beta <= alpha):
                break

        return best_score

def pacman_game(c):
    leaf_nodes = [3, 6, 2, 3, 7, 1, 2, 0]
    
    baseline_val = alpha_beta(0, 0, True, -math.inf, math.inf, leaf_nodes)
      
    left_magic_val = max(leaf_nodes[0:4]) - c
    
    right_magic_val = max(leaf_nodes[4:8]) - c
    
    best_magic_val = max(left_magic_val, right_magic_val)
    
    
    if best_magic_val > baseline_val:
        if right_magic_val > left_magic_val:
            print(f"The new minimax value is {right_magic_val}. Pacman goes right and uses dark magic")
        else:
            print(f"The new minimax value is {left_magic_val}. Pacman goes left and uses dark magic")
    else:
        print(f"The minimax value is {baseline_val}. Pacman does not use dark magic")

pacman_game(2)
pacman_game(5) 