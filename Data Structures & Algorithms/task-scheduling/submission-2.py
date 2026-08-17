from typing import List
from collections import Counter
import heapq
from collections import deque
# mathematical solution
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         array = [0] * 26
#         for c in tasks: 
#             array[ord(c) - ord('A')] += 1

#         maxf = max(array)
#         number_of_max = 0
#         for i in array: 
#             number_of_max += 1 if i == maxf else 0

#         time = (maxf - 1) * (n + 1) + number_of_max
#         return max(time, len(tasks))
#using maxheap and queue
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0 
        q = deque() #pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap: 
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: 
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
