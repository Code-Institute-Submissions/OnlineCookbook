Project Four: 

name

CRUD operators


### Version Control
1. Initial commit. Updated MongoDB, connected to database. Installed Flask. Started app.py. Deployed to Heroku.
2. Added requirements.txt and Procfile.
3. Fixed Heroku loading bug.
4. Addressed Heroku bug. Installed PyMongo. Created env.py for running the app locally, and added .gitignore so sensitive info. is not deployed.
5. Added 'get_recipes' function and 'base.html', to ensure database connection was working.
6. Added 'base.html' with layout, loaded Materialize, icons and custom.css.
7. Added working home page with get_counts and extended get_recipes functions. 
8. Started automated testing. 
9. Added search_veg and search_cuisine functions, and relevant templates. Wrote automated tests for functions so far.
10. Users can now submit recipes to the database, with the 'insert_recipe' function.
11. Users can now submit recipes to the database, with the 'insert_author' function.
12. Users can now submit recipes to the database, with the 'insert_cuisine' function.
13. Added functions to allow users to edit and delete recipes that already exist in the database.
14. Fixed 'all_recipes' bug. Added a title to the home page. Added Materialize library code, to differentiate from my code.




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

I wrote automated tests for all of the search functions, which I used with working id numbers pulled from my database. Again, I ensured the status code response was 200 and not 404.

I manually tested my get_counts function by comparing the count on my home page with the number of recipes in my database. I also wrote an automated test for this, to ensure the function worked correctly. The automated test was split into two parts, with two separate test recipe objects, with different names and counts. I used a variety of differences to ensure the function was working correctly, and used the *assertEqual* method for the correct response, and also included an incorrect response with the *assertNotEqual*. 

I manually tested the 'insert_recipe' function, by adding a recipe to the database via. the app. I could tell that it worked by searching for the recipe under the relevant categories - my name and the cuisine.

I manually tested my links, by running through every link on my page. This was successful, as I realised that I had called one of my templates *'edit_recipe.html'* in the */edit_recipe/* function, but named the template iteself *'edit_recipes.html'*, so the page would not load. I was able to fix this due to my manual testing of the app.

I also found a bug when attempting to edit a recipe under the *'all_recipes'* page. This was because the <id> of the recipe was not included in the function, so the specific recipe the user wanted to edit could not be located in the database by the unique id. I resolved this by refactoring the 'all_recipes' function, to include the unique id of each recipe.


### Bugs

I encountered a bug when trying to deploy to Heroku - the app wouldn't load. I realised this was because my requirements.txt was empty, so Heroku did not know what to load to run the app. This was because I made a mistake in the command

> pip3 freeze -- local >> requirements.txt

I realised that I had originally missed a space between '--' and 'local', which left requirements.txt empty. This taught me to always check my files before pushing to Heroku and Git Hub, because I would have realised that the file was empty and therefore the app would not load.

The push of the updated requirements.txt then caused a second error with Heroku, as I had pushed requirements that were default to the workspace, which Heroku could not load. I cleared the requirements.txt and will be manually adding to the file, so this issue does not happen in the future. 



Languages and Technologies

Materialize
