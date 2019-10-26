import praw

reddit = praw.Reddit(client_id='zQkL7caN9akLQw', client_secret='XXkY9kxR42u5LnhoJcGKe3YTtSw', user_agent='RedditPostAutoReader')

hot_posts = reddit.subreddit('AskReddit').hot(limit=1)
for post in hot_posts:
    print(post.title)
    print(post.upvote_ratio)
    print(post.is_self)
    print(post.selftext)
