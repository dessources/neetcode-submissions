class Twitter:

    def __init__(self):
        self.users = defaultdict(dict)
        self.time = 0
        """
        users : 
        {
            id: {
                    posts: [(time, id)...]
                    followees: {id:Bool}
                }
        }
        """
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.users[userId]
        if 'posts' not in user:
            user['posts'] = []
        
        heapq.heappush( user['posts'] , (-self.time, tweetId))
        self.time+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.users[userId]
        own_posts = user.get('posts', [])
        followee_posts = [self.users[id].get('posts',[]) for id in user.get('followees',{})]
        all_posts = [heapq.nsmallest(len(own_posts),own_posts)] + [heapq.nsmallest(len(p),p) for p in followee_posts]
        merged = heapq.merge(*all_posts)
        result = []
        while all_posts and len(result) < 10:
            post = next(merged, None)
            if post:
                result.append(post[1])
            else:
                break
        
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        user = self.users[followerId]
        if 'followees' not in user:
            user['followees'] = {}
        
        user['followees'][followeeId] = True
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.users[followerId].get('followees', {})
        if followeeId in followees:
            del followees[followeeId]
    
   

        
