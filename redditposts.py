import praw
from gtts import gTTS
import os
import pygame, sys, os
import pygame.camera
from pygame.locals import *
from PIL import Image, ImageDraw, ImageFont


def hopefully(imageText):

    print("testing")
    img = Image.new('RGB', (100, 30), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10,10), imageText, fill=(255,255,0))

    img.save('frame'+h+'.png')

def RedditPostAutoReader(subreddit):
    reddit = praw.Reddit(client_id='zQkL7caN9akLQw', client_secret='XXkY9kxR42u5LnhoJcGKe3YTtSw', user_agent='RedditPostAutoReader')
    popular_posts = reddit.subreddit(subreddit).hot(limit=5)
    f = open("redditPost.txt", "w+")
    posts=[]
    for post in popular_posts:
        title = (post.title)
        paragraph = (post.selftext)
        textPost = (post.is_self)
        if textPost == True:
            f.write(title+"\n" + paragraph+"\n")
            posts.append(title+"\n"+paragraph)
        else:
             print("No Description")
    print(post.upvote_ratio)
    tts = gTTS(text=title + paragraph, lang='en')
    tts.save("result.mp3")
    os.system("mpg321 result.mp3")
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
    #pygameVideo()
    hopefully()
