class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       numberStorage = {}
       for i, n in enumerate(nums): 
           difference = target - n
           if difference in numberStorage:
               return [numberStorage[difference], i]
           numberStorage[n] = i




