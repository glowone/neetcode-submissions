class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1 
        res = nums[0]

        while l <= r: 
            if nums[l] < nums[r]: 
                res = min(res, nums[l])
                break

            midpoint = (l+r) // 2
            res = min(res,nums[midpoint])
            if nums[midpoint] >= nums[l]:
                l = midpoint + 1
            else: 
                r = midpoint - 1
        return res