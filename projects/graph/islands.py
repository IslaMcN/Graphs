from util import Stack, Queue

def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if not visited[row][col]:
                if matrix[row][col] == 1:
                    visited = dft(row, col, matrix, visited)
                    island_count += 1
    return island_count


def dft(start_row, start_col, matrix, visited):
    s = Stack()
    s.push((start_row, start_col))
    while s.size() > 0:
        v = s.pop()
        row = v[0]
        col = v[1]
        if not visited[row][col]:
            visited[row][col] = True
            for n in get_neighbors(row, col, matrix):
                s.push(n)
    return visited


def get_neighbors(row, col, matrix):
    neighbors = []
    if row > 0 and matrix[row-1][col] == 1:
        neighbors.append((row-1, col))
    if row < len(matrix) - 1 and matrix[row+1][col] == 1:
        neighbors.append( (row+1, col) )
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] == 1:
        neighbors.append((row, col + 1))
    if col > 0 and matrix[row][col - 1] == 1:
        neighbors.append((row, col - 1))
    return neighbors

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))