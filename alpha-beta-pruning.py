ALPHA_INIT = 1000
BETA_INIT = -1000

def alpha_beta_search(depth, node_index, maximizing_player, node_values, alpha, beta):
    if depth == 3:
        return node_values[node_index]
    
    if maximizing_player:
        best = BETA_INIT
        for i in range(0, 2):
            val = alpha_beta_search(depth + 1, node_index * 2 + i, False, node_values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = ALPHA_INIT
        for i in range(0, 2):
            val = alpha_beta_search(depth + 1, node_index * 2 + i, True, node_values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

print("Dhruv Varshney \nA2305221157")
if __name__ == "__main__":
    node_values = [3, 5, 6, 9, 1, 2, 0, -1]
    print("The optimal value is:", alpha_beta_search(0, 0, True, node_values, BETA_INIT, ALPHA_INIT))
