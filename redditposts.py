<<<<<<< Updated upstream
import praw
from gtts import gTTS
from ffmpy import FFmpeg
import os
from PIL import Image, ImageDraw, ImageFont
import imageio
from mutagen.mp3 import MP3
def getlength(fname):
    with contextlib.closing(wave.open(fname,'r')) as f:
        return f.getnframes()
def video(posts):
    x=0
    totaltext=""
    images=[]
    for post in posts:
        x+=1
        print(x)

        length=0
        if post[1]:
            words=post[0].split(" ")
            lengths = [sum([len(words[j])+1 for j in range(i+1)]) for i in range(len(words))]
            newline = [False]+[(lengths[i-1]%100)>(lengths[i]%100) for i in range(1,len(words))]
            lines=[words[i]+" \n"[newline[i]] for i in range(len(words))]
            message="".join(lines)
        else:
            message=post[0]
        if len(message)>1500:
            posts.insert(x,(message[1500:],False))
            message=message[:1500]
        try:

            gTTS(text=message, lang="en").save("audio.mp3")
            length=int(MP3("audio.mp3").info.length)
            img = Image.new('RGB', (800, 800), color = (73, 109, 137))
            d = ImageDraw.Draw(img)
            d.text((10,10), message, fill=(255,255,0))
            img.save('frame'+str(x)+'.png')
            imgio=imageio.imread('frame'+str(x)+'.png')
            for i in range(length):
                images.append(imgio)
            totaltext+=message
        except:
            pass
    imageio.mimsave("test.gif", images, duration=1)
    print("gif")
    try:
        os.remove("silent.mp4")
    except:
        pass
    try:
        os.remove("output.mp4")
    except:
        pass
    ff=FFmpeg(executable="/usr/local/Cellar/ffmpeg/4.1.3_1/bin/ffmpeg", inputs={'test.gif': None}, outputs={'silent.mp4': None})
    print("silent")
    ff.run()
    print("done")
    gTTS(text=totaltext, lang="en").save("audio.mp3")
    os.system("/usr/local/Cellar/ffmpeg/4.1.3_1/bin/ffmpeg -i silent.mp4 -i audio.mp3 -c copy -map 0:v -map 1:a output.mp4")
def RedditPostAutoReader(subreddit,amount):
    reddit = praw.Reddit(client_id='zQkL7caN9akLQw', client_secret='XXkY9kxR42u5LnhoJcGKe3YTtSw', user_agent='RedditPostAutoReader')
    popular_posts = reddit.subreddit(subreddit).hot(limit=amount)
    #f = open("redditPost.txt", "w+")
    posts=[]
    for post in popular_posts:
        title = (post.title)
        paragraph = (post.selftext)
        textPost = (post.is_self)
        if textPost == True:
            #f.write(title+"\n" + paragraph+"\n")
            data=title+"\n"+paragraph
            posts.append((data,True))
        else:
             print("No Description")
    print(post.upvote_ratio)
    video(posts)
    #tts.save("result.wav")
    #os.system("mpg321 result.wav")
    #f.close()

def checkIfTextOrImage():
    textPost = (post.is_self)
    if textPost == "True":
          return title
    else:
         print("it didn't work")

if __name__ == '__main__':
    RedditPostAutoReader(input("Subreddit: "),int(input("Amount: ")))
=======
import praw
from gtts import gTTS
from ffmpy import FFmpeg
import os
from PIL import Image, ImageDraw, ImageFont
import imageio
from mutagen.mp3 import MP3
import re

def getlength(fname):
    with contextlib.closing(wave.open(fname,'r')) as f:
        return f.getnframes()
def video(posts):
    x=0
    totaltext=""
    images=[]
    for post in posts:
        x+=1
        print(x)

        length=0
        if post[1]:
            words=post[0].split(" ")
            lengths = [sum([len(words[j])+1 for j in range(i+1)]) for i in range(len(words))]
            newline = [False]+[(lengths[i-1]%100)>(lengths[i]%100) for i in range(1,len(words))]
            lines=[words[i]+" \n"[newline[i]] for i in range(len(words))]
            message="".join(lines)
        else:
            message=post[0]
        if len(message)>1500:
            posts.insert(x,(message[1500:],False))
            message=message[:1500]
        try:

            gTTS(text=message, lang="en").save("audio.mp3")
            length=int(MP3("audio.mp3").info.length)
            img = Image.new('RGB', (800, 800), color = (0,0,0))
            d = ImageDraw.Draw(img)
            d.text((10,10), message, fill=(255,102,25))
            img.save('frame'+str(x)+'.png')
            imgio=imageio.imread('frame'+str(x)+'.png')
            for i in range(length):
                images.append(imgio)
            totaltext+=message
        except:
            pass
    imageio.mimsave("test.gif", images, duration=1)
    print("gif")
    try:
        os.remove("silent.mp4")
    except:
        pass
    try:
        os.remove("output.mp4")
    except:
        pass
    ff=FFmpeg(executable="/usr/local/Cellar/ffmpeg/4.1.3_1/bin/ffmpeg", inputs={'test.gif': None}, outputs={'silent.mp4': None})
    print("silent")
    ff.run()
    print("done")
    print(totaltext)
    newTotalText = totaltext.replace("*", "")
    print(newTotalText)
    gTTS(text=newTotalText, lang="en").save("audio.mp3")
    os.system("/usr/local/Cellar/ffmpeg/4.1.3_1/bin/ffmpeg -i silent.mp4 -i audio.mp3 -c copy -map 0:v -map 1:a output.mp4")

def RedditPostAutoReader(subreddit,amount):
    reddit = praw.Reddit(client_id='zQkL7caN9akLQw', client_secret='XXkY9kxR42u5LnhoJcGKe3YTtSw', user_agent='RedditPostAutoReader')
    popular_posts = reddit.subreddit(subreddit).hot(limit=amount)
    #f = open("redditPost.txt", "w+")
    posts=[]
    for post in popular_posts:
        title = (post.title)
        paragraph = (post.selftext)
        textPost = (post.is_self)
        if textPost == True:
            #f.write(title+"\n" + paragraph+"\n")
            data=title+"\n"+paragraph
            posts.append((data,True))
        else:
             print("No Description")
    print(post.upvote_ratio)
    video(posts)
    #tts.save("result.wav")
    #os.system("mpg321 result.wav")
    #f.close()

def checkIfTextOrImage():
    textPost = (post.is_self)
    if textPost == "True":
          return title
    else:
         print("it didn't work")

if __name__ == '__main__':
    RedditPostAutoReader(input("Subreddit: "),int(input("Amount: ")))
>>>>>>> Stashed changes
