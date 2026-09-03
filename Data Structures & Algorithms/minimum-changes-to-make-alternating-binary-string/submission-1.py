class Solution:
    def minOperations(self, s: str) -> int:
        counter = 0 

        for i in range(len(s)): 
            if i % 2: 
                counter += 1 if s[i] == '0' else 0 
            else:
                counter += 1 if s[i] == '1' else 0 
        return min(counter, len(s) - counter)

