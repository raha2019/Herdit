import praw





def RedditPostAutoReader():
    print(input("Enter Reddit Post"))
    reddit = praw.Reddit(client_id='zQkL7caN9akLQw', client_secret='XXkY9kxR42u5LnhoJcGKe3YTtSw', user_agent='RedditPostAutoReader')
    popular_posts = reddit.subreddit('AskReddit').hot(limit=1)
    for post in popular_posts:
        title = (post.title)
        post = (post.selftext)
        if post.is_self == True:
            print(title)
            print(post)
    # print(post.upvote_ratio)
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()
