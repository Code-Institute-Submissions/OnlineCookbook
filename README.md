# HomeCooked: An Online Cook Book Database

## Project Four: Data Centric Development

This is my fourth project, an online cook book that connects to a No-SQL MongoDB database, hosted by mLabs. I want to show my proficiency in using the CRUD operators, and the app will be ran by Flask.

I wanted users to be able to upload their own recipes to the database, and also see other people's recipes for inspiration.

The app allows users to view all of the results in the database, or filter them depending on criteria, such as cuisine. I also wanted users to be able to edit recipes, incase they made any mistakes, and delete recipes if they decided they no longer wanted their information on the app.

### Demo

A live demo can be found here: https://slc-project-four.herokuapp.com/

### Technologies and Languages

* [Materialize (1.0.0)](https://materializecss.com/) - a CSS framework to make my app more visually appealing
* [jQuery(3.3)](https://jquery.com/) - a JavaScript library to enhance the user's experience
* [Javascript (1.8.5)](https://en.wikipedia.org/wiki/JavaScript) - the language and logic of the interactive elements on the page - jQuery
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - the language used to customise and present the web app, including CSS3 media queries.
* [HTML](https://en.wikipedia.org/wiki/HTML) - the language used to write and create the web app.
* [Python (3.0)](https://www.python.org/) - for backend code and site functionality.
* [MongoDB](https://www.mongodb.com/) - for my database schema
* [mLab](https://mlab.com/) - to host my MongoDB database
* [Flask (1.0.2)](http://flask.pocoo.org/) - to deploy my web application.
* [Flask-PyMongo (2.2.0)](https://flask-pymongo.readthedocs.io/) - connects Flask and Python to the MongoDB database
* [UnitTest](https://docs.python.org/3/library/unittest.html) - the Python framework for testing code


### UX

My first task was to design my database structure, as this was the basis for the entire project. I had decided to use a No-SQL database, as I would be using an SQL database in my next project, and I wanted to show my proficiency in both. 

To do this, I made a list of all of the keys I would require. I then considered which of these would be related, and decided that there would be three (cuisine, author, vegetarian). These would be the properties that would connect the data, and I would be able to use them to filter my results - ie. I could search for all vegetarian recipes. To do this, I ensured each relational property had a unique ID - so each author, cuisine, and vegetarian status had a unique ID. With these, I could loop through the options, and display the recipes that corresponded with that option. 

I also wanted to incorporate the following user stories:

* As a user, I wanted to be able to learn new recipes and retrieve my old recipes, by being able to easily store and view my recipes, as well as other people's recipes.
* As a user, I want the app to be responsive, so that I can view it on different size screens.
* As a user, I don't want to be confused by the site, so I can easily understand the function and navigation of the page.
* As a user, I want to be able to edit recipes, so that I can make changes to any that I have submitted.
* As a user, I want to be able to delete recipes, so that I can remove any content to the app that I do not want to remain on there.


### Features

* Database schema - this was based on the list of keys that I required.
* Search functions - I wanted to sort the recipes by different criteria, so that users were able to easily locate their own additions to the database, as well as retrieve new ones, so that they could try something new. I achieved this by the 'search' functions which retrieve data from the database, and include for loops to sort and return certain recipes, for example, vegetarian recipes. 
* Edit functions - I wanted user to be able to edit recipes in the database, and I achieved this with the 'edit' functions.
* Delete functions - I wanted the user to be able to delete recipes in the database, and I achieved this with the 'delete' functions. 
* Order function - I wanted the recipe lists to be ordered based on the number of 'loves' they have. I achieved this by sorting the lists with the *'itemgetter'* function from *'operator'*, and then reversing the result, because by default, the numbers ascend and I wanted the recipe with the most 'loves' to be first.
* Detailed views of each recipe - I wanted the user to be able to drill down into each recipe in the lists. This was because I didn't want to overload the page with too many recipes, as this would frustrate the user. This would also increase the loading time for the page and use more internet data to load. I wanted the user to be able to choose which recipes they wanted to see more of, so I created collapsible menus, which could be clicked to reveal the whole recipe.
* Media queries - I wanted the app to be responsive so it did not matter what size screen the user was viewing it on, so I used media queries to customise the CSS depending on the screen size. 
* Materialize - I used the framework of Materialize to make my app look visually appealing, so that the user does not get confused by the page or is put off by a bad design. 

In the future, I would work on adding user registration and authentication to the app, so that users would only be able to edit and delete the recipes that they have submitted. 

I would also like to implement a 'like' system, similar to the feature on Facebook, where users can click to 'like' specific recipes.

### Deployment

My code is deployed to GitHub, at: https://github.com/sarahcrosby/OnlineCookbook

I have also deployed my code to Heroku, at: https://slc-project-four.herokuapp.com/

To run the app locally, download the files from GitHub and upload to your workspace. Then, ensure you follow the requirements.txt and install everything indicated in this. 

Alternatively, you could clone the repository, by typing the following command into the terminal:

> $ git clone https://github.com/sarahcrosby/OnlineCookbook

You will then be able to run the app by typing the following into the terminal:

> python3 app.py run

My mLabs database would not be accessible when the code is ran locally, so you would need to set up a new database and add data. To do this, change the app configuration on lines 9 and 10 of app.py to connect to your database.

### Testing

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

I tested how the code worked on different screen sizes, by using the emulator 
function in the developer tools, and also on my mobile device, laptop and 
tablet. During this manual test, I realised that I had added custom CSS that made the menu box on every page look very small on mobile devices, because it was set to 50% across every screen size. To fix this, I added CSS3 media queries, so that the custom CSS for *'.menu-box'* was different across the different screen sizes.

I encountered a bug when trying to deploy to Heroku - the app wouldn't load. I realised this was because my requirements.txt was empty, so Heroku did not know what to load to run the app. This was because I made a mistake in the command

> pip3 freeze -- local >> requirements.txt

I realised that I had originally missed a space between '--' and 'local', which left requirements.txt empty. This taught me to always check my files before pushing to Heroku and Git Hub, because I would have realised that the file was empty and therefore the app would not load.

The push of the updated requirements.txt then caused a second error with Heroku, as I had pushed requirements that were default to the workspace, which Heroku could not load. I cleared the requirements.txt and will be manually adding to the file, so this issue does not happen in the future.

Before pushing my code for the final time, I decided to do a final manual test of my code, by trying every link again and seeing if I could 'break' the app. I am glad that I did this, as I discovered a bug with the *'search_veg'* function. The count of vegetarian recipes was appearing, but when I drilled into this, the comment 'There does not currently appear to be any vegetarian recipes' appeared, which I included as an if conditional on *'search_veg.html'* to be printed if there were no recipes of that kind in the database. I realised this was because I had accidentally deleted the following line of code from *'app.py'*, from the *'search-veg'* function:

> veg_recipes.append(recipe_obj)

This meant that the *'veg_recipes'* list was empty, as nothing was being appended to it, and the for loop on *'search_veg.html'* was therefore empty. I resolved this by adding the line of code back in.

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
13. Added functions to allow users to edit and delete recipes that already exist in the database. Fixed 'all_recipes' bug. Added a title to the home page. Added Materialize library code, to differentiate from my code.
14. Completed library of code. Added media queries.
15. Worked on README.md, and also added comments to code for clarity.
16. Final edits to code. Turned debug mode off.