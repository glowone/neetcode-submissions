class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        array = [0] * 26
        for c in tasks: 
            array[ord(c) - ord('A')] += 1

        maxf = max(array)
        number_of_max = 0
        for i in array: 
            number_of_max += 1 if i == maxf else 0

        time = (maxf - 1) * (n + 1) + number_of_max
        return max(time, len(tasks))