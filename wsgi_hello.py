from wsgiref.simple_server import make_server

# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style environment variables and the
# second variable is the callable object (see PEP 333).
def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/html; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    # The returned object is going to be printed
    return [b"""<!DOCTYPE html>
    <html>
    <head>
    <title>Lets Create a page and do the fun stuff!</title>
    <style>
    Body {background-color: skyblue;}
    h1 {color: darkblue;
    font-family: verdana;
    font-size: 140%;
    }
    p {color: red;
    font-family: courier;
    font-size: 150%;
    }
    h2 {color: blue;
    }
    </style>
    </head>
    <body>
    <center>
    <h1>First of were going to add in some more wording, maybe some pictures if its possible and a lot of more letters and words.</h1>
    <p>At the start of a paragraph you should introduce yourself, well I'm kevin and I'm going to comment as much as I can for a while, but for the mean time, enjoy the sentences</p>
    <p>Hello, World! Well not so much since if you think about life for a second we are in terrible state where we can't help the planet as much and were destroying it even more, the business people are the rulers of the time in a monopoly state of mind, labor worldwide, racism and all the dangerous activities as well.</p>
    <h2>RUN THE SERVER BOYO.</h2>
    </center>
    </body>
    </html>"""]

with make_server('', 3000, hello_world_app) as httpd:
    print("Loading up on port 3000...")

    # Serve until process is killed
    httpd.serve_forever()