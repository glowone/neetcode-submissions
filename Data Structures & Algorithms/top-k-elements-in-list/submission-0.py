class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #can use hashmap to store frequency of numbers 
        #list from top to bottom 
        #depending on integer k, we output how many top appearing numbers we want to show up 

        count = {} 
        freq = [ [] for i in range(len(nums) + 1)]

        for n in nums: 
            count[n] = 1 + count.get(n,0)
        for n, c in count.items(): 
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1): 
            for n in freq[i]: 
                res.append(n)
                if len(res) == k:
                    return res