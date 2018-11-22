import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from operator import itemgetter

# Loads Flask and PyMongo, and loads database
app = Flask(__name__)
app.config["MONGO_DB"] = 'project-four'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


# Function that loops through a list and returns how many items are in that list in the format of a dictionary that prints the type of item and the count of that item.
def get_counts(recipes, individual_item, list_of_items):
    item_counts = [0 for i in list_of_items]
    i=0
    while i < len(list_of_items):
        j=0
        while j < len(recipes):
            item = recipes[j][str(individual_item)].lower()
            if item == list_of_items[i]:
                item_counts[i] += 1
            j += 1
        i += 1
    return dict(zip(list_of_items, item_counts))
    

# Returns the home page, which used the get_counts function to list the number of different types of recipes, so the user can drill down into their chosen categories.
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    
    # Retrieves the data from the database
    recipes = mongo.db.recipes.find()
    cuisine_list_looped = mongo.db.cuisine_list.find()
    vegetarian_list_looped=mongo.db.vegetarian_list.find()
    author_list_looped=mongo.db.authors_list.find()
    recipe_objects = [recipe for recipe in recipes]
    
    # Creates a list of the different cuisines, and uses the 'get_count' function to return a dictionary of the cuisine names with a count of how many recipes are in the database under that cuisine
    cuisine_names = [cuisine['cuisine_name'].lower() for cuisine in cuisine_list_looped]
    cuisine_counts = get_counts(recipe_objects, 'cuisine_name', cuisine_names)
    
    # Creates a list of the different authors, and uses the 'get_count' function to return a dictionary of the authors with a count of how many recipes in the database that they submitted
    authors_names = [auth['author'].lower() for auth in author_list_looped]
    author_counts = get_counts(recipe_objects, 'author_name', authors_names)
    
    # Creates a list of all of the vegetarian recipes in the database, and returns a dictionary including the number of vegetarian recipes
    veg_type = [veg['vegetarian'].lower() for veg in vegetarian_list_looped]
    veg_counts = get_counts(recipe_objects, 'recipe_is_vegetarian', veg_type)
    
    return render_template("recipes.html", 
    recipes=recipes,
    cuisine_list = mongo.db.cuisine_list.find(),
    authors_list=mongo.db.authors_list.find(),
    vegetarian_list=mongo.db.vegetarian_list.find(),
    veg_counts=veg_counts,
    cuisine_counts=cuisine_counts, 
    author_counts = author_counts,
    all_recipe_count = mongo.db.recipes.count())
    

# Function that returns all of the recipes in the database, and renders them to 'all_recipes.html'
@app.route('/all_recipes/')
def all_recipes():
    recipes = mongo.db.recipes.find()
    all_recipes_list = []
    
    # Loops through all of the recipes, and appends each object to a new list
    for recipe in recipes:
            recipe_obj = {
                'recipe_obj': recipe,
                'recipe_loves': recipe['recipe_loves'],
                'author_name': recipe['author_name'],
                'recipe_id': recipe['_id'],
                'recipe_name': recipe['recipe_name'],
                'cuisine_name': recipe['cuisine_name'],
                'recipe_description': recipe['recipe_description'],
                'recipe_ingredients': recipe['recipe_ingredients'],
                'recipe_method': recipe['recipe_method'],
                'recipe_is_vegetarian': recipe['recipe_is_vegetarian']
            }
            all_recipes_list.append(recipe_obj)
    
    # Sorts the recipes list by the number of loves each recipe has, starting with the highest at the top        
    all_recipes_list = sorted(all_recipes_list, key=itemgetter("recipe_loves"), reverse=True)
    return render_template('all_recipes.html', recipes=recipes, all_recipes_list=all_recipes_list)

            
# Function that returns all of the vegetarian recipes and renders them to 'search_veg.html'
@app.route('/search_veg/<veg_id>')
def search_veg(veg_id):
    expand_veg = mongo.db.vegetarian_list.find_one({"_id": ObjectId(veg_id)})
    recipes = mongo.db.recipes.find()
    veg_recipes = []
    for recipe in recipes:
        
        # Loops through all of the recipes, and appends each object to a new list
        if recipe['recipe_is_vegetarian'] == expand_veg['vegetarian']:
            recipe_obj = {
                'recipe_obj': recipe,
                'recipe_loves': recipe['recipe_loves'],
                'author_name': recipe['author_name'],
                'recipe_id': recipe['_id'],
                'recipe_name': recipe['recipe_name'],
                'cuisine_name': recipe['cuisine_name'],
                'recipe_description': recipe['recipe_description'],
                'recipe_ingredients': recipe['recipe_ingredients'],
                'recipe_method': recipe['recipe_method'],
                'recipe_is_vegetarian': recipe['recipe_is_vegetarian']
            }
            veg_recipes.append(recipe_obj)
    # Sorts the recipes list by the number of loves each recipe has, starting with the highest at the top
    veg_recipes = sorted(veg_recipes, key=itemgetter("recipe_loves"), reverse=True)
    return render_template('search_veg.html', veg_recipes=veg_recipes, veg=expand_veg, recipes=mongo.db.recipes.find())
    

# Function that returns all of the recipes by cuisine and renders them to 'search_cuisine.html' 
@app.route('/search_cuisine/<cuisine_id>')
def search_cuisine(cuisine_id):
    expand_cuisine = mongo.db.cuisine_list.find_one({"_id": ObjectId(cuisine_id)})
    recipes = mongo.db.recipes.find()
    cuisine_recipes = []
    for recipe in recipes:
        
        # Loops through all of the recipes, and appends each object to a new list
        if recipe['cuisine_name'] == expand_cuisine['cuisine_name']:
            recipe_obj = {
                'recipe_obj': recipe,
                'recipe_loves': recipe['recipe_loves'],
                'author_name': recipe['author_name'],
                'recipe_id': recipe['_id'],
                'recipe_name': recipe['recipe_name'],
                'cuisine_name': recipe['cuisine_name'],
                'recipe_description': recipe['recipe_description'],
                'recipe_ingredients': recipe['recipe_ingredients'],
                'recipe_method': recipe['recipe_method'],
                'recipe_is_vegetarian': recipe['recipe_is_vegetarian']
            }
            cuisine_recipes.append(recipe_obj)
    
    # Sorts the recipes list by the number of loves each recipe has, starting with the highest at the top   
    cuisine_recipes = sorted(cuisine_recipes, key=itemgetter("recipe_loves"), reverse=True)
    return render_template('search_cuisine.html', cuisine_recipes=cuisine_recipes, cuisine=expand_cuisine, recipes=mongo.db.recipes.find())


# Function that returns all of the recipes by a particular author and renders them to 'search_author.html' 
@app.route('/search_author/<author_id>')
def search_author(author_id):
    expand_author = mongo.db.authors_list.find_one({"_id": ObjectId(author_id)})
    recipes = mongo.db.recipes.find()
    author_recipes = []
    for recipe in recipes:
        
        # Loops through all of the recipes, and appends each object to a new list
        if recipe['author_name'] == expand_author['author']:
            recipe_obj = {
                'recipe_obj': recipe,
                'recipe_loves': recipe['recipe_loves'],
                'author_name': recipe['author_name'],
                'recipe_id': recipe['_id'],
                'recipe_name': recipe['recipe_name'],
                'cuisine_name': recipe['cuisine_name'],
                'recipe_description': recipe['recipe_description'],
                'recipe_ingredients': recipe['recipe_ingredients'],
                'recipe_method': recipe['recipe_method'],
                'recipe_is_vegetarian': recipe['recipe_is_vegetarian']
            }
            author_recipes.append(recipe_obj)
    
    # Sorts the recipes list by the number of loves each recipe has, starting with the highest at the top   
    author_recipes = sorted(author_recipes, key=itemgetter("recipe_loves"), reverse=True)
    return render_template('search_author.html', author_recipes=author_recipes, author=expand_author, recipes=mongo.db.recipes.find())
    
    
# Renders a page where users can add recipes to the database
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
     cuisine_list=mongo.db.cuisine_list.find(),
     authors_list=mongo.db.authors_list.find())


# Adds user's input into the database using the POST method, from a form on 'add_recipe.html'
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


# Renders a page where users can add their name as an author to the database
@app.route('/add_author')
def add_author():
    return render_template('add_author.html')
    
    
# Adds user's input into the database using the POST method, from a form on 'add_author.html'
@app.route('/insert_author', methods=['POST'])
def insert_author():
    authors_list =  mongo.db.authors_list
    authors_list.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
    
# Renders a page where users can add a type of cuisine to the database
@app.route('/add_cuisine')
def add_cuisine():
    return render_template('add_cuisine.html')
    
    
# Adds user's input into the database using the POST method, from a form on 'add_cuisine.html'
@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisine_list =  mongo.db.cuisine_list
    cuisine_list.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
    
# Renders a page where users can edit recipes already in the database
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines =  mongo.db.cuisine_list.find()
    all_authors = mongo.db.authors_list.find()
    return render_template('edit_recipe.html', recipe=the_recipe, cuisine_list=all_cuisines, authors_list=all_authors)
  
  
# Updates the existing recipe in the database with the user's input, using the POST method from a form on 'edit_recipe.html'
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get['recipe_name'],
        'cuisine_name':request.form.get['cuisine_name'],
        'author_name': request.form.get['author_name'],
        'description': request.form.get['recipe_description'],
        'ingredients':request.form.get['recipe_ingredients'],
        'method':request.form.get['recipe_method'],
        'recipe_is_vegetarian':request.form.get['recipe_is_vegetarian'],
        'recipe_loves':request.form.get['recipe_loves']
    })
    return redirect(url_for('get_recipes'))
 
 
# Allows a user to delete a recipe from the database
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes')) 


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=False)