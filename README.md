### Version Control
1. Initial commit. Updated MongoDB, connected to database. Installed Flask. Started app.py. Deployed to Heroku.
2. Added requirements.txt and Procfile.
3. Fixed Heroku loading bug.
4. Addressed Heroku bug. Installed PyMongo. Created env.py for running the app locally, and added .gitignore so sensitive info. is not deployed.




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

### Bugs

I encountered a bug when trying to deploy to Heroku - the app wouldn't load. I realised this was because my requirements.txt was empty, so Heroku did not know what to load to run the app. This was because I made a mistake in the command

> pip3 freeze -- local >> requirements.txt

I realised that I had originally missed a space between '--' and 'local', which left requirements.txt empty. This taught me to always check my files before pushing to Heroku and Git Hub, because I would have realised that the file was empty and therefore the app would not load.

I then had an issue with Flask ...