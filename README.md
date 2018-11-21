### Version Control
1. Initial commit. Updated MongoDB, connected to database. Installed Flask. Started app.py. Deployed to Heroku.
2. Added requirements.txt and Procfile.
3. Fixed Heroku loading bug.
4. Addressed Heroku bug. Installed PyMongo. Created env.py for running the app locally, and added .gitignore so sensitive info. is not deployed.
5. Added 'get_recipes' function and 'base.html', to ensure database connection was working.
6. Added 'base.html' with layout, loaded Materialize, icons and custom.css.
7. Added working home page with get_counts and extended get_recipes functions. 
8. Started automated testing. 




### Tests

The first test I created was when I first started the project, and has since been deleted. This was a simple 'Hello World' function, to test whether the set up was working. This was in the form of the following: 

>import os
>
>from flask import Flask
>
>app =Flask(__name__)
>
>@app.route('/')
>
>def hello():
>
>    return 'Hello World!'
>    
>if __name__ == '__main__':
>
>    app.run(host=os.environ.get('IP'),
>
>   port=int(os.environ.get('PORT')),
>
>    debug=True)

I then manually checked whether the database was correctly linked to the app, by creating the following function that finds all of the recipes in my database:

>@app.route('/')
>
>@app.route('/get_recipes')
>
>def get_recipes():
>
>    return render_template("recipes.html", recipes=mongo.db.recipes.find())

Then I added a loop on 'recipes.html' to print the recipes names. When I ran my app, all of the recipes names were listed on the page, so I knew my dabase was correctly loaded.

I created my first unit tests after implementing the home page. I started by testing that the tests themselves were working, by asserting that 1 and 1 were equal. I followed this by testing the status codes of the app, to ensure the response status code did return with 200, and did not return with a 404.

I manually tested my get_counts function by comparing the count on my home page with the number of recipes in my database.



### Bugs

I encountered a bug when trying to deploy to Heroku - the app wouldn't load. I realised this was because my requirements.txt was empty, so Heroku did not know what to load to run the app. This was because I made a mistake in the command

> pip3 freeze -- local >> requirements.txt

I realised that I had originally missed a space between '--' and 'local', which left requirements.txt empty. This taught me to always check my files before pushing to Heroku and Git Hub, because I would have realised that the file was empty and therefore the app would not load.

The push of the updated requirements.txt then caused a second error with Heroku, as I had pushed requirements that were default to the workspace, which Heroku could not load. I cleared the requirements.txt and will be manually adding to the file, so this issue does not happen in the future. 