import praw





def RedditPostAutoReader(subreddit):
    reddit = praw.Reddit(client_id='zQkL7caN9akLQw', client_secret='XXkY9kxR42u5LnhoJcGKe3YTtSw', user_agent='RedditPostAutoReader')
    popular_posts = reddit.subreddit(subreddit).hot(limit=1)
    for post in popular_posts:
        title = (post.title)
        text = (post.selftext)
        if post.is_self():
            print(title)
            print(text)
            return text
    # print(post.upvote_ratio
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()
