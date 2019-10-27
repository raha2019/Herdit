from bottle import route, request, run, static_file
import redditposts
@route('/', method="GET")
def form():
    return '''
        <html>
            <head>
                    <style>
                    body{
                            background: #FFFFFF;
                            background: -moz-linear-gradient(top, #7d8570 0%, #646F58 66%, #504B3A 100%);
                            background: -webkit-linear-gradient(top, #7d8570 0%, #646F58 66%, #504B3A 100%);
                            background: linear-gradient(to bottom, #7d8570 0%, #646F58 66%, #504B3A 100%);
                            text-align:center;
                            color: #000000;
                            font-family: arial;

                    }
                    h1{
                            color: #FFFFFF;
                            background: -moz-linear-gradient(top, #afbe8f 0%, #7d8570 86%, #646F58 100%);
                            background: -webkit-linear-gradient(top, #afbe8f 0%, #7d8570 86%, #646F58 100%);
                            background: linear-gradient(to bottom, #afbe8f 0%, #7d8570 86%, #646F58 100%);
                            text-shadow: 4px 3px 0 #7A7A7A;
                            font-size:100;
                    }
                    form {
                        margin: 0;
                        background: white;
                        position: absolute;
                            padding:30px;
                            border:10px solid #000000;
                            background: #FFFFFF;
                            background: -moz-linear-gradient(top, #afbe8f 0%, #7d8570 86%, #646F58 100%);
                            background: -webkit-linear-gradient(top, #afbe8f 0%, #7d8570 86%, #646F58 100%);
                            background : linear-gradient(to bottom, #afbe8f 0%, #7d8570 86%, #646F58 100%);
                        top: 50%;
                        left: 50%;
                        margin-right: -50%;
                        transform: translate(-50%, -50%);
                            text-align:center;
                    }
                    #submit{
                            background: #FFFFFF;
                            background: -moz-linear-gradient(top, #dde392 0%, #afbe8f 86%, #7d8570 100%);
                            background: -webkit-linear-gradient(top, #dde392 0%, #afbe8f 86%, #7d8570 100%);
                            background: linear-gradient(to bottom, #dde392 0%, #afbe8f 86%, #7d8570 100%);
                    }
u                    </style>
                    <title>Herdit!</title>
            </head>
            <body>
                    <h1>Herdit!</h1>
                    <form action="/sendsub" method="POST">
                      Subreddit: <input type="text" name="reddit" value="">
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
    print(request.forms.get('reddit'))
    redditposts.RedditPostAutoReader(request.forms.get('reddit'))
    return static_file("result.mp3", root="")
run(host='localhost', port=9999)
