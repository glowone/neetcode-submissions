from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # This handles days where a warmer temp is never found.
        numbers = [0] * len(temperatures)
        
        for t in range(len(temperatures)):
            for n in range(t + 1, len(temperatures)):
                if temperatures[n] > temperatures[t]:
                    
                    # The number of days is just the difference in their indices
                    numbers[t] = n - t
                    break
        return numbers