from bottle import route, request, run, static_file
import redditposts
@route('/', method="GET")
def form():
    return '''
        <html>
            <head>
                    <style>
                    body{
                            background: #F19953;
                            text-align:center;
                            color: #000000;
                            font-family: arial;
                            
                    }
                    h1{
                            
                            text-shadow: 4px 3px 0 #7A7A7A;
                            font-size:100;
                    }
                    .left {
                        padding: 0px 30px;
                        display:block;
                        float: left;
                    }
                    .right {
                        padding: 0px 30px;
                        display:block;
                        float: right;
                    }
                    p{
                            color: #FFFFFF;
                            font-size: 20;
                            text-shadow: 4px 3px 0 #7A7A7A;
                    }
                    form {
                        margin: 0;
                        background: white;
                        color:#EDF7F6;
                        position: absolute;
                            padding:30px 60px;
                            border:10px outset #999999;
                            background: #FF6622;
                        top: 50%;
                        left: 50%;
                        margin-right: -50%;
                        transform: translate(-50%, -50%);
                            text-align:center;
                    }
                    #submit{
                            margin:50px;
                            padding:10px;
                            vertical-align:bottom;
                            background: #EDF7F6;
                    }
u                    </style>
                    <title>Herdit!</title>
            </head>
            <body>
                    <h1>Herdit!</h1>
                    <form action="/sendsub" method="POST">
                      <span class="left">
                        <p>Enter Story Subreddit:</p>
                        <input type="text" name="reddit" value="">
                      </span>
                      <div class="right">
                        <p>Enter Number of Stories:</p>
                        <input type="text" name="amount" value="">
                      </div>
                      <br>
                      <br>
                      <br>
                      <input type="submit" id="submit" value="Let me Heerit!">
                    </form>
            </body>
        </html>
    '''
@route('/sendsub',method="GET")
@route('/sendsub',method="POST")
def sendsub():
    #print(request.forms.get('reddit'))
    try:
        redditposts.RedditPostAutoReader(request.forms.get('reddit'),request.forms.get('amount'))
    except:
        pass
    if os.name == 'nt':
        return static_file("result.mp3", root=".\\")
    return static_file("result.mp3", root="./")
run(host='localhost', port=9999)
