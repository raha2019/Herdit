import praw
import requests
import re
import pytesseract
from gtts import gTTS
import os
import json
from PIL import Image, ImageDraw, ImageFont


def downloadImage(amount): #Done after 2AM
    a = open('dankmemes.json')
    dankmemes = json.loads(a.read())
    dankmemes2 = dankmemes.get('data')
    dankmemes3 = dankmemes2.get('children')
    for i in range(amount):
        dankmemes4 = dankmemes3[i]
        dankmemes5 = dankmemes4.get('data')
        img_url = dankmemes5.get('url')
        print(str(img_url))




def video(imageText):
    print("testing")
    img = Image.new('RGB', (100, 30), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10,10), imageText, fill=(255,255,0))

    img.save('frame'+h+'.png')

def RedditPostAutoReader(subreddit,amount):
    reddit = praw.Reddit(client_id='zQkL7caN9akLQw', client_secret='XXkY9kxR42u5LnhoJcGKe3YTtSw', user_agent='RedditPostAutoReader')
    popular_posts = reddit.subreddit(subreddit).hot(limit=amount)
    f = open("redditPost.txt", "w+")
    posts=[]
    for post in popular_posts:
        title = (post.title)
        paragraph = (post.selftext)
        textPost = (post.is_self)
        if textPost == True:
            f.write(title+"\n" + paragraph+"\n")
            posts.append(title+"\n"+paragraph)
        elif textPost == False:
            get_image(popular_posts)
        else:
             print("No Description")
    tts = gTTS(text="\n\n".join(posts),lang='en')
    tts.save("result.wav")
    os.system("mpg321 result.wav")
    f.close()

amount = 10
if __name__ == '__main__':
    #RedditPostAutoReader(subreddit,5)
    downloadImage(amount)
