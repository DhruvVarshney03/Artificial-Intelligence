import heapq

print("Dhruv Varshney \nA2305221157\n")
def heuristic(state, goal):
    return sum(abs(b % 3 - g % 3) + abs(b // 3 - g // 3) for b, g in zip(state, goal))

def find_blank_tile(state):
    return state.index(0)

def swap_tiles(state, i1, i2):
    state = list(state)
    state[i1], state[i2] = state[i2], state[i1]
    return tuple(state)

def get_possible_moves(state):
    blank_index = find_blank_tile(state)
    row, col = blank_index // 3, blank_index % 3
    moves = []
    if row > 0:
        moves.append(swap_tiles(state, blank_index, blank_index - 3))  # Up
    if row < 2:
        moves.append(swap_tiles(state, blank_index, blank_index + 3))  # Down
    if col > 0:
        moves.append(swap_tiles(state, blank_index, blank_index - 1))  # Left
    if col < 2:
        moves.append(swap_tiles(state, blank_index, blank_index + 1))  # Right
    return moves

def best_first_search(start, goal):
    explored = set()
    frontier = []
    heapq.heappush(frontier, (0, start))
    parents = {}
    
    while frontier:
        priority, state = heapq.heappop(frontier)
        if state == goal:
            return reconstruct_path(parents, start, state)
        
        explored.add(state)
        
        for move in get_possible_moves(state):
            if move not in explored:
                parents[move] = state
                heapq.heappush(frontier, (heuristic(move, goal), move))
    
    return None  # No solution found

def reconstruct_path(parents, start, goal):
    path = []
    state = goal
    
    while state != start:
        path.append(state)
        state = parents[state]
    
    path.append(start)  # Add the start state at the beginning
    path.reverse()      # Reverse the path to get the correct order
    
    return path

def print_path(path):
    for i, state in enumerate(path):
        print(f"Move {i+1}:")
        for row in [state[i:i+3] for i in range(0, 9, 3)]:
            print(row)
        
        if i < len(path) - 1:
            blank_index = find_blank_tile(state)
            blank_row, blank_col = blank_index // 3, blank_index % 3
            next_blank_index = find_blank_tile(path[i+1])
            next_blank_row, next_blank_col = next_blank_index // 3, next_blank_index % 3
            
            print(f"Move blank tile {'up' if blank_row > next_blank_row else 'down' if blank_row < next_blank_row else 'left' if blank_col > next_blank_col else 'right'}\n")

if __name__ == "__main__":
    start_matrix = []
    
    for i in range(3):
        row = list(map(int, input(f"Enter row {i+1} of the starting matrix (space-separated): ").split()))
        start_matrix.extend(row)
    
    goal_matrix = []
    
    for i in range(3):
        row = list(map(int, input(f"Enter row {i+1} of the goal matrix (space-separated): ").split()))
        goal_matrix.extend(row)
    
    solution = best_first_search(tuple(start_matrix), tuple(goal_matrix))
    
    if solution:
        print("Solution found:")
        print_path(solution)
    
    else:
        print("No solution found.")