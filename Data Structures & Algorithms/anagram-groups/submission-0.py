from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = defaultdict(list) 

        for s in strs: 
            count = [0] * 26
            for c in s: 
                count[ord(c) - ord("a")] += 1
            
            values[tuple(count)].append(s)
        return list(values.values())
