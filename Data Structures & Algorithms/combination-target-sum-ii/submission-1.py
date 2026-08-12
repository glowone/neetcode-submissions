from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        # Sort to group duplicates together
        candidates.sort()
        
        def dfs(i, cur, total): 
            if total == target:
                res.append(cur.copy())
                return 
            
            if i >= len(candidates) or total > target: 
                return 
            
            # --- DECISION 1: INCLUDE candidates[i] ---
            # We include it without skipping. This allows us to use [2, 2, 2] if needed.
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            # --- DECISION 2: EXCLUDE candidates[i] ---
            cur.pop()
            
            # Now that we decided NOT to use candidates[i], we must skip all identical 
            # numbers next to it so we don't build duplicate combinations.
            # (Notice the bounds check: i + 1 < len(candidates))
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: 
                i += 1
                
            dfs(i + 1, cur, total) 
            
        dfs(0, [], 0)
        return res