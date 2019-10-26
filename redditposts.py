import praw
from gtts import gTTS
import os
import pygame, sys, os
import pygame.camera
from pygame.locals import *

def pygameVideo():

    pygame.init()
    pygame.camera.init()

    try:
        os.makedirs("Snaps")
    except OSError:
        pass
    screen = pygame.display.set_mode((640, 480))

    cam = pygame.camera.Camera("/dev/video0", (640, 480))
    cam.start()
    print("")


def RedditPostAutoReader(subreddit):
    reddit = praw.Reddit(client_id='zQkL7caN9akLQw', client_secret='XXkY9kxR42u5LnhoJcGKe3YTtSw', user_agent='RedditPostAutoReader')
    popular_posts = reddit.subreddit(subreddit).hot(limit=5)
    f = open("redditPost.txt", "w+")
    for post in popular_posts:
        title = (post.title)
        paragraph = (post.selftext)
        textPost = (post.is_self)
        if textPost == True:
            f.write(title+"\n" + paragraph+"\n")
            tts = gTTS(text=title + paragraph, lang='en')
            tts.save("result.mp3")
            os.system("mpg321 result.mp3")
        else:
             print("No Description")
    print(post.upvote_ratio)
    f.close()
def checkIfTextOrImage():
    textPost = (post.is_self)
    if textPost == "True":
          return title
    else:
         print("it didn't work")

if __name__ == '__main__':
    user_input = "nosleep"
    subreddit = user_input
    #RedditPostAutoReader(subreddit)
    pygameVideo()
