import math

def minimax_search(cur_depth, node_index, is_max_turn, node_values, target_depth):

    # Base case: targetDepth reached
    if cur_depth == target_depth:
        return node_values[node_index]

    if is_max_turn:
        return max(minimax_search(cur_depth + 1, node_index * 2, False, node_values, target_depth),
                   minimax_search(cur_depth + 1, node_index * 2 + 1, False, node_values, target_depth))

    else:
        return min(minimax_search(cur_depth + 1, node_index * 2, True, node_values, target_depth),
                   minimax_search(cur_depth + 1, node_index * 2 + 1, True, node_values, target_depth))

# Driver code
node_values = [3, 5, 2, 9, 12, 5, 23, 23]

tree_depth = math.log(len(node_values), 2)

print("Dhruv Varshney \nA2305221157")
print("The optimal value is:", end=" ")
print(minimax_search(0, 0, True, node_values, tree_depth))
