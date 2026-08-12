class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        scandidates = sorted(candidates)
        def dfs(i, cur, total): 
            if total == target:
                res.append(cur.copy())
                return 
            
            if i >= len(scandidates) or total > target: 
                return 
            #include candidate and skip to next
            cur.append(scandidates[i])
            dfs(i+1, cur, total + scandidates[i])

            cur.pop()
            while i + 1 < len(scandidates) and scandidates[i] == scandidates[i + 1]: 
                i += 1
            dfs(i+1, cur, total) 
        dfs(0,[],0)
        return res