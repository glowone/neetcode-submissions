class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums) 
        

        array = [[] for i in range(len(nums) * 2)] 

        for i in range(length):
            array[i] = nums[i]
        for i in range(length, len(array)):
            array[i] = nums[i-length]
        return array

        