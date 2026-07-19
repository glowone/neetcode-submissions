#return true if strings are anagrams of each other, otherwise return false 

#anagrams contain same exact letters as another string but order can be different 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        countS, countT = {}, {} #initializing hashmaps for s and t 

        for i in range(len(s)): 
            countS[s[i]] = 1 + countS.get(s[i], 0) #increment count of character in string s at index i 
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS: 
            if countS[c] != countT.get(c,0): 
                return False 
        
        return True