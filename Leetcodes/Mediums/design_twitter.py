from collections import defaultdict
import heapq
from typing import List

class Twitter:
    def __init__(self):
        # Counter to track tweet chronology (decreasing to use min-heap for newest first)
        self.count = 0
        # Store tweets by user: userTweets[userId] = [(count, tweetId), ...]
        self.userTweets = defaultdict(list)
        # Store who each user follows: userFollows[userId] = {followeeId1, followeeId2, ...}
        self.userFollows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add tweet to user's tweet list with current timestamp
        self.userTweets[userId].append((self.count, tweetId))
        self.count -= 1  # Decrement to ensure newer tweets have smaller count

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        result = []
        
        # Each user follows themselves by default
        follows = self.userFollows[userId].copy()
        follows.add(userId)
        
        # Add the latest tweet from each followed user to the heap
        for followeeId in follows:
            if followeeId in self.userTweets and self.userTweets[followeeId]:
                tweets = self.userTweets[followeeId]
                idx = len(tweets) - 1  # Index of the most recent tweet
                count, tweetId = tweets[idx]
                # Store (count, tweetId, followeeId, idx) in the heap
                heapq.heappush(minheap, (count, tweetId, followeeId, idx))
        
        # Get the 10 most recent tweets
        while minheap and len(result) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minheap)
            result.append(tweetId)
            
            # Check if there are more tweets from this user
            idx -= 1
            if idx >= 0:
                count, tweetId = self.userTweets[followeeId][idx]
                heapq.heappush(minheap, (count, tweetId, followeeId, idx))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)