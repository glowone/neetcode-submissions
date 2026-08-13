class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS= len(board), len(board[0])
        path = set() #data structure for our path, to make sure we don't revisit the same position twice

        def dfs(r, c, i):
            if i == len(word): #solution case 
                return True
            if (r < 0 or c < 0 or r >= ROWS 
                or c >= COLS or word[i] != board[r][c] 
                or (r,c) in path):
                return False

            path.add((r,c))
            res = (dfs(r + 1, c, i +1) or 
            dfs(r - 1, c, 1 +i) or 
            dfs(r, c + 1, 1 +i) or 
            dfs(r, c - 1, 1 +i))       
            path.remove((r,c))
            return res       

        for r in range(ROWS): 
            for c in range(COLS): 
                if dfs(r,c,0): 
                    return True   
        return False 