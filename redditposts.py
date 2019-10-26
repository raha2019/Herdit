import praw


def RedditPostAutoReader(subreddit):
    reddit = praw.Reddit(client_id='zQkL7caN9akLQw', client_secret='XXkY9kxR42u5LnhoJcGKe3YTtSw', user_agent='RedditPostAutoReader')
    popular_posts = reddit.subreddit(subreddit).hot(limit=3)
    f = open("redditPost.txt", "w+")
    for post in popular_posts:
        title = (post.title)
        paragraph = (post.selftext)
        textPost = (post.is_self)
        # if textPost:
        #      return title
        # else:
        #     print(title)
        # return paragraph
        #print("didn't work")
    # print(post.upvote_ratio
        f.write(title+"\n" + paragraph+"\n")
    f.close()



if __name__ == '__main__':
    user_input = "nosleep"
    subreddit = user_input
    RedditPostAutoReader(subreddit)
