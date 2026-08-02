from typing import List 
##my solution, works but is O(n+m logn+m) runtime :(
# class Solution: 
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 
#         nums3 = nums1 + nums2
#         nums3 = sorted(nums3)
#         l = 0 
#         r = len(nums3) - 1
#         midpoint = 0

#         #if we have even numbers
#         if len(nums3) % 2 == 0: 
#             while l < r:
#                 l += 1
#                 r -= 1
#             midpoint = (nums3[l] + nums3[r]) / 2
#             return midpoint
#         if len(nums3) % 2 == 1: 
#             midpoint = (l + r)//2 
#             return nums3[midpoint]

# neetcode proper binary search solution

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1 
        B = nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A): 
            A, B = B, A

        l = 0 
        r = len(A) - 1
        while True: 
            i = (l + r) // 2 #A
            j = half - i - 2 #B

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1