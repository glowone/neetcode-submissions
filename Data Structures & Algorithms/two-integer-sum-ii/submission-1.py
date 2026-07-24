#brute force sol - works with O(n^2) time complexity
# from typing import List

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for n in range(len(numbers)):
#             for s in range(len(numbers)): 
#                 if numbers[n] + numbers[s] == target: 
#                     return [n+1,s+1]


#two pointer sol 
from typing import List
class Solution: 
    def twoSum(self,numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r: 
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target: 
                l += 1
            if numbers[l] + numbers[r] == target: 
                return [l+1, r+1]