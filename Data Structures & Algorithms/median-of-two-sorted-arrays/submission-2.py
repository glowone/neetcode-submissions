class Solution: 
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 
        nums3 = nums1 + nums2
        nums3 = sorted(nums3)
        l = 0 
        r = len(nums3) - 1
        midpoint = 0

        #if we have even numbers
        if len(nums3) % 2 == 0: 
            while l < r:
                l += 1
                r -= 1
            midpoint = (nums3[l] + nums3[r]) / 2
            return midpoint
        if len(nums3) % 2 == 1: 
            midpoint = (l + r)//2 
            return nums3[midpoint]