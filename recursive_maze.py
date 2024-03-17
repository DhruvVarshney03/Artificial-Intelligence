import numpy as np

def maze_creation(n):
    maze = np.random.randint(2, size=(n, n))
    maze[0][0] = 1
    maze[n-1][n-1] = 1
    return maze

def maze_traverse(array, current_pos, target_pos, visited):
    row, col = current_pos

    if current_pos == target_pos:
        return True

    if 0 <= row < len(array) and 0 <= col < len(array[0]) and array[row, col] == 1 and tuple(current_pos) not in visited:
        visited.append(tuple(current_pos))
        array[row, col] = 2

        if (maze_traverse(array, [row-1, col], target_pos, visited) or
            maze_traverse(array, [row+1, col], target_pos, visited) or
            maze_traverse(array, [row, col-1], target_pos, visited) or
            maze_traverse(array, [row, col+1], target_pos, visited)):
            return True

    return False

n = int(input("Enter the size of array: "))
maze = maze_creation(n)
print("maze:\n", maze)

current = [0, 0]
target = [n-1, n-1]

visited_pos = []
if maze_traverse(maze, current, target, visited_pos):
    maze[target[0], target[1]] = 2
    print("\nMaze traversed successfully!")
else:
    print("\nMaze traversal failed.")

print("\nAfter traversal:")
print(maze)
