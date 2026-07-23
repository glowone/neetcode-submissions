#given a 9x9 sudoku board we have to determine whether the board is valid or not
# each row must contain digits 1-9 without repetition 
# each column must contain digits 1-9 without repetition 
# each of the nine 3x3 sub-boxes of the grid must contain digits 1-9 without repetition 

# 1. we will have a unique hashset for every row to check for duplicates
# 2. we will have a unique hashset for every column to check for duplicates 
# 3. can have a unique hashset to represent every 3x3 grid to check for duplicates, but how do we ensure each hashset
# is unique to its 3by3 grid? 
import collections  
class Solution: 
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue #skips value 
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r //3, c//3)]): 
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
