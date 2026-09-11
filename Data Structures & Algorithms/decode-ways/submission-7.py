class Solution:
    def numDecodings(self, s: str) -> int:
        dp2 = 0
        dp1 = 1
        for i in range(len(s)-1, -1, -1):
            dp = 0 if s[i] == '0' else dp1
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] < '7'):
                dp += dp2
            dp1, dp2 = dp, dp1
        return dp1

            
                