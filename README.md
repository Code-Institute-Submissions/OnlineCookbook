### Version Control
1. Initial commit. Updated MongoDB, connected to database. Installed Flask. Started app.py. Deployed to Heroku.
2. 




### Tests

The first test I created was when I first started the project, and has since been deleted. This was a simple 'Hello World' function, to test whether the set up was working. This was in the form of the following: 

>import os
>from flask import Flask
>
>app =Flask(__name__)
>
>@app.route('/')
>def hello():
>    return 'Hello World!'
>    
>if __name__ == '__main__':
>    app.run(host=os.environ.get('IP'),
>   port=int(os.environ.get('PORT')),
>    debug=True)