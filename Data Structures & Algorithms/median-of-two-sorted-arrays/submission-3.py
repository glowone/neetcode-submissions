class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        p1 = 0
        p2 = 0
        
        # 1. Traverse both arrays, picking the smaller number each time
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                nums3.append(nums1[p1])
                p1 += 1
            else:
                nums3.append(nums2[p2])
                p2 += 1
                
        # 2. If one array was longer, append the remaining elements
        # (Only one of these extends will actually add anything)
        nums3.extend(nums1[p1:])
        nums3.extend(nums2[p2:])
        
        # 3. Find the median using direct index math
        n = len(nums3)
        midpoint = n // 2
        
        if n % 2 == 0:
            # If even, take the average of the two middle elements
            return (nums3[midpoint - 1] + nums3[midpoint]) / 2.0
        else:
            # If odd, return the exact middle element
            return float(nums3[midpoint])