class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # iterate throug each index
        # all all neighbors of current index to queue 
        # check all neighbors at same time to see if water can flow through 

        ROWS, COLS = len(heights), len(heights[0]) 
        pac, atl = set(), set() 

        def dfs(r,c,visit,prevHeight): 
            if ((r,c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS-1])
        
        for c in range(COLS): 
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])

        res = [] 
        for r,c in (pac & atl): 
            res.append([r,c])
        return res

        


         