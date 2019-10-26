import praw





def RedditPostAutoReader(subreddit):
    reddit = praw.Reddit(client_id='zQkL7caN9akLQw', client_secret='XXkY9kxR42u5LnhoJcGKe3YTtSw', user_agent='RedditPostAutoReader')
    popular_posts = reddit.subreddit(subreddit).hot(limit=1)
    for post in popular_posts:
        title = (post.title)
        paragraph = (post.selftext)
        #textPost = (post.is_self)
        # if textPost:
        #     return title
        # else:
        print(title)
        return paragraph
        #print("didn't work")
    # print(post.upvote_ratio
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()
