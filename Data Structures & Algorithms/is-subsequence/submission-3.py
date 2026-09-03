class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0 
        r = 0
        count = 0 
        length_first = len(s)
        length_second = len(t)

        if len(s) == 0:
            return True
        if len(t) == 0: 
            return False
        while l <= r: 
            if s[l] and t[r] and s[l] == t[r]: 
                count += 1 
                r += 1
                l += 1
            else: 
                r += 1
            if count == length_first:
                return True
            if r == length_second:
                return False


