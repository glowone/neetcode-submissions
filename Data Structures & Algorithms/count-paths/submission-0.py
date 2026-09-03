# Dynamic Programming - Time: O(n * m), Space: O(m), where m is num of cols
class Solution:
    def uniquePaths(self, rows, cols):
        row = [1] * cols

        for i in range(rows-1):
            newRow = [1] * cols 
            for j in range(cols-2,-1,-1): 
                newRow[j] = newRow[j+1] + row[j]
            row = newRow 
        return row[0]
