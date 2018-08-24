# coding: utf8
"""
---------------------------------------------
    File Name: Twitter
    Description: 
    Author: wangdawei
    date:   2018/1/18
---------------------------------------------
    Change Activity: 
                    2018/1/18
---------------------------------------------    
"""

class User:
    def __init__(self, id):
        self.id = id
        self.tweets = []
        self.followers = set([])

    def postTweet(self, tweetId):
        self.tweets.append(tweetId)

    def follow(self, followeeId):
        self.followers.add(followeeId)

    def unfollow(self, followeeId):
        if followeeId in self.followers:
            self.followers.remove(followeeId)


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.tweets = []

    def _addUser(self, userId):
        if userId not in self.users:
            user = User(userId)
            self.users[userId] = user

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """

        self._addUser(userId)
        self.tweets.append(tweetId)
        self.users[userId].postTweet(len(self.tweets)-1)


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        self._addUser(userId)
        user = self.users[userId]
        ulist = user.followers.copy()
        ulist.add(userId)
        tweets = []
        for uid in ulist:
            userT = self.users[uid]
            tweets.extend(userT.tweets[-10:])
        tweets = [self.tweets[ti] for ti in sorted(tweets)[-1:-11:-1]]
        return tweets

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self._addUser(followerId)
        self._addUser(followeeId)
        self.users[followerId].follow(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self._addUser(followerId)
        self._addUser(followeeId)
        self.users[followerId].unfollow(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

def main():
    twitter = Twitter()
    twitter.postTweet(1, 6)
    print(twitter.getNewsFeed(1))
    twitter.follow(1, 2)
    twitter.postTweet(2, 5)
    print(twitter.getNewsFeed(1))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))

if __name__ == "__main__":
    main()