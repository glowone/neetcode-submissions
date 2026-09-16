class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1): 
            for t in range(i + 1, len(nums)): 
                if nums[i] < nums[t]: 
                    LIS[i] = max(LIS[i], 1 + LIS[t])
        return max(LIS)