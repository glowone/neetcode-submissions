class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set() 
        count = 0 

        for c in s: 
            if c in seen: 
                seen.remove(c)
                count += 2 
            else: 
                seen.add(c)
        if seen: 
            count += 1 
        return count