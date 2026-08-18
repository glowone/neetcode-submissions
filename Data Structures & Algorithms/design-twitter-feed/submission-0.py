from typing import List
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)  # user_id -> list of [count, tweet_id]
        self.follow_map = defaultdict(set)  # user_id -> set of followee_ids

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.follow_map[userId].add(userId)
        for followee_id in self.follow_map[userId]:
            if followee_id in self.tweet_map:
                index = len(self.tweet_map[followee_id]) - 1
                count, tweet_id = self.tweet_map[followee_id][index]
                min_heap.append([count, tweet_id, followee_id, index - 1])
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            count, tweet_id, followee_id, index = heapq.heappop(min_heap)
            res.append(tweet_id)
            if index >= 0:
                count, tweet_id = self.tweet_map[followee_id][index]
                heapq.heappush(min_heap, [count, tweet_id, followee_id, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)