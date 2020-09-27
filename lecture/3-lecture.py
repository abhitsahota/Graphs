'''
Finding connected components demo

Leetcode #200, Number of Islands

If node is located adjacent to another node they are considered connected, but if it is diagonal it is not. Assume we're using a 2d matrix to vizualize this problem.
'''
'''
Plan
1. Translate the problem into graph terminology
each vertex is a cell, the edge, is the neighbouring cell
traverse the grid (double for loop probably needed)
if we find a 1, 
    increment numislands, 
    then we want to traverse all of it's connected components
and mark them as visited
return num islands


'''

from collections import deque


def numIslands(self, grid: List[List[str]]) -> int:

    num = 0

    # input check if it is zero
    if len(grid) == 0:
        return 0

    width, height = len(grid[0]), len(grid)
    visited = [[False] * width for x in range(height)] # we don't use a set because we received a matrix as the input not a dictionary

    # use a double for loop to traverse the list
    for y in range(height):
        for x in range(width):

            if grid[y][x] == '1' and not visited[y][x]:
                num +=1
                markConnectedComponentsAsVisited(grid, visited, x, y)

    return num

# start at x, y and mark components that are '1' as visited
def markConnectedComponentsAsVisited(grid, visited, x, y):

    width, height = len(grid[0]), len(grid)
    stack = deque
    stack.append((x, y))
    while len(stack) > 0:
        x, y = stack.pop()
        if visited[y][x]:
            continue
        visited[y][x] = True
        # Traverse all adjacent nodes that are also 1
        if x -1 >= 0 and grid[y][x-1] == '1':
            stack.append((x-1, y))
        if x + 1 < width and grid[y][x + 1] == '1':
            stack.append((x+1, y))
        if y -1 >= 0 and grid[y-1][x] == '1':
            stack.append((x, y-1))
        if y+1 < height and grid[y+1][x] == '1':
            stack.append((x, y+1))
