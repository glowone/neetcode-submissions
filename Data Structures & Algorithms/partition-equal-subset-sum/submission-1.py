class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: 
            return False
        dp = set() 
        target = sum(nums)//2
        dp.add(0) 

        for i in range(len(nums)-1,-1,-1): 
            newDP = set()
            for t in dp: 
                newDP.add(t + nums[i]) 
                newDP.add(t) 
            dp = newDP
        return True if target in dp else False