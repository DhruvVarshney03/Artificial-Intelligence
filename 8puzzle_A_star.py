import heapq
import numpy as np

class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
    
    def __lt__(self, other):
        return self.f < other.f

def misplaced_tiles(state, goal):
    count = np.sum(state != goal)
    return count

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i, j] != 0:  # Skip the empty tile
                current_row, current_col = np.where(state == state[i, j])
                goal_row, goal_col = np.where(goal == state[i, j])
                distance += abs(int(current_row) - int(goal_row)) + abs(int(current_col) - int(goal_col))
    return distance

def solve(initial_state, goal_state):
    open_set = []
    closed_set = set()
    start_node = Node(initial_state, None, 0, misplaced_tiles(initial_state, goal_state))
    heapq.heappush(open_set, start_node)
    
    while open_set:
        current_node = heapq.heappop(open_set)
        
        if np.array_equal(current_node.state, goal_state):
            return current_node
        
        closed_set.add(tuple(map(tuple, current_node.state)))
        
        for child_state in generate_child_states(current_node.state):
            child_node = Node(child_state, current_node, current_node.g + 1,
                              misplaced_tiles(child_state, goal_state) + manhattan_distance(child_state, goal_state))
            
            if tuple(map(tuple, child_node.state)) not in closed_set:
                heapq.heappush(open_set, child_node)
    
    return None

def generate_child_states(state):
    child_states = []
    empty_tile_index = np.where(state == 0)
    possible_moves = [
        (empty_tile_index[0] - 1, empty_tile_index[1]),
        (empty_tile_index[0] + 1, empty_tile_index[1]),
        (empty_tile_index[0], empty_tile_index[1] - 1),
        (empty_tile_index[0], empty_tile_index[1] + 1)
    ]
    
    for move in possible_moves:
        i, j = move
        
        if 0 <= i < 3 and 0 <= j < 3:
            new_state = np.copy(state)
            new_state[empty_tile_index], new_state[i, j] = new_state[i, j], new_state[empty_tile_index]
            child_states.append(new_state)
    
    return child_states

def print_solution(node):
    path = []
    
    while node:
        path.append(node.state)
        node = node.parent
    
    path.reverse()
    
    for state in path:
        print(state)

if __name__ == "__main__":
    print("Dhruv Varshney \nA2305221157")
    initial_state = np.array([[1, 2, 3], [5, 6, 0], [7, 8, 4]])
    goal_state = np.array([[1, 2, 3], [5, 8, 6], [0, 7, 4]])
    
    solution_node = solve(initial_state, goal_state)
    
    if solution_node:
        print("Solution found:")
        print_solution(solution_node)
    
    else:
        print("No solution found.")