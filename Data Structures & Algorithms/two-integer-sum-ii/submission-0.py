from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in range(len(numbers)):
            for s in range(len(numbers)): 
                if numbers[n] + numbers[s] == target: 
                    return [n+1,s+1]