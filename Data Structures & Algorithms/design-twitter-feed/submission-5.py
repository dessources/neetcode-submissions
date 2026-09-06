class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0
       

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.posts[userId]
        user.append([-self.time, tweetId, userId])
        self.time+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        ids = [userId] + [followeeId for followeeId in self.users[userId]]
       
        heap = [self.posts[i][-1]+[1] for i in ids if self.posts[i]]
     
        heapq.heapify(heap)
        result = []
        while heap and len(result) < 10:
            time, postId, user, rank = heapq.heappop(heap)
            result.append(postId)
            if rank+1 <= len(self.posts[user]):
                new_post = self.posts[user][-(rank+1)]+[rank+1]
                heapq.heappush(heap, new_post)
           
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
    
   

        
