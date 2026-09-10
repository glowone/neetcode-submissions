class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 

        for i in range(len(s)): 
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                res += 1
                l -= 1
                r += 1
            left, right = i, i+1 
            while left >= 0 and right<len(s) and s[left] == s[right]: 
                res += 1
                left -= 1 
                right += 1
        return res
