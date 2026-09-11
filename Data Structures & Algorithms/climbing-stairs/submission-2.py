class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: 
            return 1
        if n == 2: 
            return 2 
        
        ways = [0] * (n+1) 

        ways[1] = 1
        ways[2] = 2 

        for n in range(3, n+1): 
            ways[n] = ways[n-1] + ways[n-2]
        return ways[n]