class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums) 
        

        array = [[] for i in range(len(nums) * 2)] 

        for i, num in enumerate(nums): 
            array[i] = array[i+length] = num
        return array

        