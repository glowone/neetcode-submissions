from collections import deque
from typing import List
        #check for rotten fruit
        #once found, traverse all adjacent fruits
        #can we have multiple rotting fruits?
        #if multiple rotting fruits, are they all adjacent? 
        #return min of adjacent fuits? 

        # sol: keep track of how many fresh oranges there are initially
        # in case you have isolated orange you will know and return -1
        # otherwise, take all rotten oranges append to q and do level order traversal

        #O(m*n) time and memory complexity 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1: 
                    fresh += 1
                if grid[r][c] == 2: 
                    q.append([r,c]) 

        directions = [[0,1], [0, -1], [1,0], [-1,0]]
        while q and fresh > 0: 
            
            for i in range(len(q)): 
                r, c = q.popleft()
                for dr, dc in directions: 
                    row, col = dr + r, dc + c

                    if (row < 0 or row == len(grid) or 
                        col < 0 or col == len(grid[0]) or 
                        grid[row][col] != 1): 
                        continue

                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
                


        
        