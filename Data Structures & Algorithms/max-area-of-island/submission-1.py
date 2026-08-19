from typing import List
import collections

#bfs sol 
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
#         if not grid: 
#             return 0 

#         rows, cols = len(grid), len(grid[0])
#         visit = set()
#         area = 0

#         def bfs(r,c): #remember bfs is iterative, use queue
#             q = collections.deque()
#             visit.add((r,c))
#             q.append((r,c))
#             newarea = 1

#             while q: 
#                 row, col = q.popleft()
#                 directions = [[1,0], [-1, 0], [0,1], [0, -1]]
#                 for dr, dc in directions:
#                     rah, cah = row + dr, col + dc
#                     if ((rah) in range(rows) and
#                         (cah) in range(cols) and 
#                         grid[rah][cah] == 1 and 
#                         (rah, cah) not in visit): 
#                         q.append((rah, cah))
#                         visit.add((rah, cah))
#                         newarea += 1        
#             return newarea


#         for r in range(rows): 
#             for c in range(cols):
#                 if grid[r][c] == 1 and (r,c) not in visit: 
#                     area = max(area, bfs(r,c))
#         return area 


#dfs sol 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0 

        rows, cols = len(grid), len(grid[0]) 
        visit = set()

        def dfs(r,c):
           if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in visit): 
               return 0
           visit.add((r,c))
           return (1 + dfs(r + 1, c) +
                   dfs(r - 1, c) + 
                   dfs(r, c + 1) +
                   dfs(r, c - 1))
        area = 0
        for r in range(rows):
            for c in range(cols): 
                area = max(area, dfs(r,c))
        return area


